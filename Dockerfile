#
# Build image
#
from rust:1.41-slim as build

WORKDIR /app

RUN rustup target add x86_64-unknown-linux-musl

RUN apt-get update && apt-get install -y musl-tools \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/*

COPY api/Cargo.lock api/Cargo.toml ./api/

RUN mkdir ./api/.cargo
RUN cd api && cargo vendor > .cargo/config

RUN rustup show active-toolchain

COPY ./ ./

RUN cd api && cargo build --release --target x86_64-unknown-linux-musl

#
# Final image
#
FROM scratch

COPY --from=build /app/api/target/x86_64-unknown-linux-musl/release/api /usr/local/bin/

USER 1000

EXPOSE 8000

CMD ["/usr/local/bin/api"]
