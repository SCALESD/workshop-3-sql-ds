
/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


# Dump of table parking-meter-location
# ------------------------------------------------------------

CREATE TABLE `parking-meter-location` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `zone` varchar(32) DEFAULT NULL,
  `area` varchar(64) DEFAULT NULL,
  `sub_area` varchar(128) DEFAULT NULL,
  `pole` varchar(16) DEFAULT NULL,
  `config_id` int(11) DEFAULT NULL,
  `config_name` varchar(96) DEFAULT NULL,
  `longitude` double DEFAULT NULL,
  `latitude` double DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `longitude` (`longitude`),
  KEY `latitude` (`latitude`),
  KEY `zone` (`zone`),
  KEY `sub_area` (`sub_area`),
  KEY `pole` (`pole`),
  KEY `config_name` (`config_name`),
  KEY `config_id` (`config_id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;



# Dump of table parking-meter-transaction
# ------------------------------------------------------------

CREATE TABLE `parking-meter-transaction` (
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `uuid` varchar(48) DEFAULT NULL,
  `meter_type` varchar(12) DEFAULT NULL,
  `pole_id` varchar(16) DEFAULT NULL,
  `trans_amt` int(11) DEFAULT NULL,
  `pay_method` varchar(16) DEFAULT NULL,
  `trans_start` datetime DEFAULT NULL,
  `meter_expire` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uuid_2` (`uuid`),
  KEY `pole_id` (`pole_id`),
  KEY `trans_start` (`trans_start`),
  KEY `meter_expire` (`meter_expire`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;




/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
