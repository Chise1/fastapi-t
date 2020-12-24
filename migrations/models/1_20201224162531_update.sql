##### upgrade #####
CREATE TABLE IF NOT EXISTS `permission` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `label` VARCHAR(128) NOT NULL,
    `model` VARCHAR(128) NOT NULL,
    `codename` VARCHAR(128) NOT NULL
) CHARACTER SET utf8mb4 COMMENT='must inheritance AbstractPermission';;
CREATE TABLE IF NOT EXISTS `role` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `label` VARCHAR(50) NOT NULL
) CHARACTER SET utf8mb4 COMMENT='must inheritance AbstractRole';;
CREATE TABLE IF NOT EXISTS `user` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `username` VARCHAR(20) NOT NULL UNIQUE,
    `password` VARCHAR(200) NOT NULL,
    `is_active` BOOL NOT NULL  DEFAULT 1,
    `is_superuser` BOOL NOT NULL  DEFAULT 0,
    `last_login` DATETIME(6) NOT NULL  COMMENT 'Last Login',
    `avatar` VARCHAR(200) NOT NULL  DEFAULT '',
    `intro` LONGTEXT NOT NULL,
    `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6)
) CHARACTER SET utf8mb4;;
##### downgrade #####
DROP TABLE IF EXISTS `permission`;
DROP TABLE IF EXISTS `role`;
DROP TABLE IF EXISTS `user`;
