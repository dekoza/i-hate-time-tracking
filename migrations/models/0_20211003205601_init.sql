-- upgrade --
CREATE TABLE IF NOT EXISTS "reporters" (
    "id" CHAR(36) NOT NULL  PRIMARY KEY,
    "slug" VARCHAR(100) NOT NULL,
    "description" TEXT NOT NULL,
    "enabled" INT NOT NULL  DEFAULT 1
) /* Which plugin reported the entry. */;
CREATE INDEX IF NOT EXISTS "idx_reporters_slug_4e163d" ON "reporters" ("slug");
CREATE TABLE IF NOT EXISTS "sessions" (
    "id" CHAR(36) NOT NULL  PRIMARY KEY,
    "description" TEXT NOT NULL,
    "start" TIMESTAMP,
    "end" TIMESTAMP
) /* Used to group Entries */;
CREATE TABLE IF NOT EXISTS "entries" (
    "id" CHAR(36) NOT NULL  PRIMARY KEY,
    "description" TEXT NOT NULL,
    "timestamp" TIMESTAMP NOT NULL,
    "reporter_id" CHAR(36) REFERENCES "reporters" ("id") ON DELETE CASCADE,
    "session_id" CHAR(36) REFERENCES "sessions" ("id") ON DELETE CASCADE
) /* A single entry in the worklog. Can be grouped using Sessions. */;
CREATE INDEX IF NOT EXISTS "idx_entries_timesta_aee1f9" ON "entries" ("timestamp");
CREATE TABLE IF NOT EXISTS "aerich" (
    "id" INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    "version" VARCHAR(255) NOT NULL,
    "app" VARCHAR(20) NOT NULL,
    "content" JSON NOT NULL
);
