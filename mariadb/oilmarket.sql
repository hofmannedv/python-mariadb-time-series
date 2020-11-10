-- MySQL dump 10.17  Distrib 10.3.23-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: oilmarket
-- ------------------------------------------------------
-- Server version	10.3.23-MariaDB-0+deb10u1

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `exchangegbp`
--

DROP TABLE IF EXISTS `exchangegbp`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `exchangegbp` (
  `timestamp` datetime DEFAULT NULL,
  `value` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exchangegbp`
--

LOCK TABLES `exchangegbp` WRITE;
/*!40000 ALTER TABLE `exchangegbp` DISABLE KEYS */;
/*!40000 ALTER TABLE `exchangegbp` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `exchangeusd`
--

DROP TABLE IF EXISTS `exchangeusd`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `exchangeusd` (
  `timestamp` datetime DEFAULT NULL,
  `value` float DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `exchangeusd`
--

LOCK TABLES `exchangeusd` WRITE;
/*!40000 ALTER TABLE `exchangeusd` DISABLE KEYS */;
/*!40000 ALTER TABLE `exchangeusd` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `marketdata`
--

DROP TABLE IF EXISTS `marketdata`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `marketdata` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `date` datetime DEFAULT NULL,
  `sortid` int(11) DEFAULT NULL,
  `close` float DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=881617 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `marketdata`
--

LOCK TABLES `marketdata` WRITE;
/*!40000 ALTER TABLE `marketdata` DISABLE KEYS */;
/*!40000 ALTER TABLE `marketdata` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `oilsort`
--

DROP TABLE IF EXISTS `oilsort`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `oilsort` (
  `grade` varchar(255) DEFAULT NULL,
  `market` varchar(255) DEFAULT NULL,
  `publisher` varchar(255) DEFAULT NULL,
  `instrument` varchar(255) DEFAULT NULL,
  `description` varchar(255) DEFAULT NULL,
  `id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `oilsort`
--

LOCK TABLES `oilsort` WRITE;
/*!40000 ALTER TABLE `oilsort` DISABLE KEYS */;
/*!40000 ALTER TABLE `oilsort` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-11-02  2:09:54
