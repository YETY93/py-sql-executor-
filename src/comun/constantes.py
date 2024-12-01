# Directorio base para archivos de ambiente
PATH_AMBIENTES: str = "./data/"

# Directorio que contiene los scripts de configuración CSV
PATH_CONFIG_CSV: str = "./configScript/"
INICIAL_NOMBRE_CSV: str = "configScript"
EXTENSION_CSV: str = ".csv"
CABECERA_FORMAT_CSV: str = "ID;AUTOR;NOMBRE_ARCHIVO_SQL"

# Sript inicial sql archivo configurracion
PATH_SQL: str = "./sql/"
SCRIPT_INICIAL_NOMBRE_SQL: str = "sqlInicial"
EXTENSION_SQL: str = ".sql"
SCRIPT_INICIAL_SQL: str = """CREATE TABLE `config_py_sql_executor` (
    `id` INT UNSIGNED NOT NULL,
    `autor` VARCHAR(50) NOT NULL,
    `nombre_archivo_sql` VARCHAR(200) NOT NULL,
    `hash_archivo` VARCHAR(200) NOT NULL,
    UNIQUE INDEX `idx_id` (`id`), -- Índice único para `id`
    UNIQUE INDEX `idx_nombre_archivo` (`nombre_archivo_sql`) -- Índice único para `nombre_archivo_sql`
)
COLLATE='utf8mb4_general_ci'; """
