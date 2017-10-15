CREATE TABLE "data" (
  "id" integer PRIMARY KEY AUTOINCREMENT NOT NULL,
  "timestamp" datetime NOT NULL,
  "temperature" float(128) NOT NULL,
  "humidity" float(128) NOT NULL
);
