#[macro_use]
extern crate lazy_static;

use chrono::prelude::*;

use actix_cors::Cors;
use actix_web::{get, web, App, HttpRequest, HttpResponse, HttpServer, Responder};
use serde::{Deserialize, Serialize};

const NATIONAL_RAW: &str = include_str!("../../dati-json/dpc-covid19-ita-andamento-nazionale.json");
const REGIONS_RAW: &str = include_str!("../../dati-json/dpc-covid19-ita-regioni.json");
const PROVINCES_RAW: &str = include_str!("../../dati-json/dpc-covid19-ita-province.json");

lazy_static! {
    static ref NATIONAL: Vec<NationalItem> = serde_json::from_str(&NATIONAL_RAW).unwrap();
    static ref REGIONS: Vec<RegionsItem> = serde_json::from_str(&REGIONS_RAW).unwrap();
    static ref PROVINCES: Vec<ProvincesItem> = serde_json::from_str(&PROVINCES_RAW).unwrap();
}

mod rfc3339_time {
    use chrono::NaiveDateTime;
    use serde::{self, Deserialize, Deserializer, Serializer};

    const FORMAT: &'static str = "%Y-%m-%d %H:%M:%S";

    pub fn serialize<S: Serializer>(
        date: &NaiveDateTime,
        serializer: S,
    ) -> Result<S::Ok, S::Error> {
        let s = format!("{}", date.format(FORMAT));
        serializer.serialize_str(&s)
    }

    pub fn deserialize<'de, D: Deserializer<'de>>(
        deserializer: D,
    ) -> Result<NaiveDateTime, D::Error> {
        let s = String::deserialize(deserializer)?;
        NaiveDateTime::parse_from_str(&s, FORMAT).map_err(serde::de::Error::custom)
    }
}

#[derive(Clone, Serialize, Deserialize)]
struct NationalItem {
    #[serde(with = "rfc3339_time")]
    data: NaiveDateTime,
    stato: String,
    ricoverati_con_sintomi: u32,
    terapia_intensiva: u32,
    totale_ospedalizzati: u32,
    isolamento_domiciliare: u32,
    totale_attualmente_positivi: u32,
    nuovi_attualmente_positivi: i32,
    dimessi_guariti: u32,
    deceduti: u32,
    totale_casi: u32,
    tamponi: u32,
}

#[derive(Deserialize)]
struct Period {
    begin: Option<NaiveDateTime>,
    end: Option<NaiveDateTime>,
}

#[get("/andamento-nazionale")]
async fn national(period: web::Query<Period>) -> impl Responder {
    return match (period.begin, period.end) {
        (Some(begin), None) => HttpResponse::Ok().json(
            NATIONAL
                .iter()
                .filter(|item| item.data >= begin)
                .cloned()
                .collect::<Vec<NationalItem>>(),
        ),
        (None, Some(end)) => HttpResponse::Ok().json(
            NATIONAL
                .iter()
                .filter(|item| item.data <= end)
                .cloned()
                .collect::<Vec<NationalItem>>(),
        ),
        (Some(begin), Some(end)) => HttpResponse::Ok().json(
            NATIONAL
                .iter()
                .filter(|item| item.data >= begin && item.data <= end)
                .cloned()
                .collect::<Vec<NationalItem>>(),
        ),
        (None, None) => HttpResponse::Ok()
            .content_type("application/json")
            .body(NATIONAL_RAW),
    };
}

#[derive(Clone, Serialize, Deserialize)]
struct ProvincesItem {
    #[serde(with = "rfc3339_time")]
    data: NaiveDateTime,
    stato: String,
    codice_regione: u16,
    denominazione_regione: String,
    codice_provincia: u16,
    denominazione_provincia: String,
    sigla_provincia: String,
    lat: f64,
    long: f64,
    totale_casi: u32,
}
async fn provinces(req: HttpRequest, period: web::Query<Period>) -> impl Responder {
    let province = req.match_info().query("province");
    let region = req.match_info().query("region");

    fn province_matches(item: &ProvincesItem, province: &str) -> bool {
        if province.is_empty() {
            return true;
        }
        item.denominazione_provincia == province
    }
    fn region_matches(item: &ProvincesItem, region: &str) -> bool {
        if region.is_empty() {
            return true;
        }
        item.denominazione_regione == region
    }

    return match (period.begin, period.end) {
        (Some(begin), None) => HttpResponse::Ok().json(
            PROVINCES
                .iter()
                .filter(|item| {
                    item.data >= begin
                        && province_matches(item, province)
                        && region_matches(item, region)
                })
                .cloned()
                .collect::<Vec<ProvincesItem>>(),
        ),
        (None, Some(end)) => HttpResponse::Ok().json(
            PROVINCES
                .iter()
                .filter(|item| {
                    item.data <= end
                        && province_matches(item, province)
                        && region_matches(item, region)
                })
                .cloned()
                .collect::<Vec<ProvincesItem>>(),
        ),
        (Some(begin), Some(end)) => HttpResponse::Ok().json(
            PROVINCES
                .iter()
                .filter(|item| {
                    item.data >= begin
                        && item.data <= end
                        && province_matches(item, province)
                        && region_matches(item, region)
                })
                .cloned()
                .collect::<Vec<ProvincesItem>>(),
        ),
        (None, None) => HttpResponse::Ok().json(
            PROVINCES
                .iter()
                .filter(|item| province_matches(item, province) && region_matches(item, region))
                .cloned()
                .collect::<Vec<ProvincesItem>>(),
        ),
    };
}

#[derive(Clone, Serialize, Deserialize)]
struct RegionsItem {
    #[serde(with = "rfc3339_time")]
    data: NaiveDateTime,
    stato: String,
    codice_regione: u16,
    denominazione_regione: String,
    lat: f64,
    long: f64,
    ricoverati_con_sintomi: u32,
    terapia_intensiva: u32,
    totale_ospedalizzati: u32,
    isolamento_domiciliare: u32,
    totale_attualmente_positivi: u32,
    nuovi_attualmente_positivi: i32,
    dimessi_guariti: u32,
    deceduti: u32,
    totale_casi: u32,
    tamponi: u32,
}

async fn regions(req: HttpRequest, period: web::Query<Period>) -> impl Responder {
    let region = req.match_info().query("region");

    fn region_matches(item: &RegionsItem, region: &str) -> bool {
        if region.is_empty() {
            return true;
        }
        item.denominazione_regione == region
    }

    return match (period.begin, period.end) {
        (Some(begin), None) => HttpResponse::Ok().json(
            REGIONS
                .iter()
                .filter(|item| item.data >= begin && region_matches(item, region))
                .cloned()
                .collect::<Vec<RegionsItem>>(),
        ),
        (None, Some(end)) => HttpResponse::Ok().json(
            REGIONS
                .iter()
                .filter(|item| item.data <= end && region_matches(item, region))
                .cloned()
                .collect::<Vec<RegionsItem>>(),
        ),
        (Some(begin), Some(end)) => HttpResponse::Ok().json(
            REGIONS
                .iter()
                .filter(|item| {
                    item.data >= begin && item.data <= end && region_matches(item, region)
                })
                .cloned()
                .collect::<Vec<RegionsItem>>(),
        ),
        (None, None) => HttpResponse::Ok().json(
            REGIONS
                .iter()
                .filter(|item| region_matches(item, region))
                .cloned()
                .collect::<Vec<RegionsItem>>(),
        ),
    };
}

#[actix_rt::main]
async fn main() -> std::io::Result<()> {
    println!("Listening on 0.0.0.0:8000");

    HttpServer::new(|| {
        App::new()
            .wrap(Cors::new().finish())
            .service(national)
            .service(
                web::scope("/province")
                    .service(web::resource("").to(provinces))
                    .service(web::resource("/{region}").to(provinces))
                    .service(web::resource("/{region}/{province}").to(provinces)),
            )
            .service(
                web::scope("/regioni")
                    .service(web::resource("").to(regions))
                    .service(web::resource("/{region}").to(regions)),
            )
    })
    .bind("0.0.0.0:8000")?
    .run()
    .await
}
