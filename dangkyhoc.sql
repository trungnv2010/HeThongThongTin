-- MySQL dump 10.13  Distrib 8.0.33, for Win64 (x86_64)
--
-- Host: localhost    Database: tuition_fee
-- ------------------------------------------------------
-- Server version	8.0.33

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `dangkyhoc`
--

DROP TABLE IF EXISTS `dangkyhoc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dangkyhoc` (
  `ma_dang_ky_hoc` varchar(255) NOT NULL,
  `ma_sv` varchar(255) DEFAULT NULL,
  `ma_mon_hoc` varchar(255) DEFAULT NULL,
  `ky_hoc` varchar(255) DEFAULT NULL,
  `ngay_dang_ky` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ma_dang_ky_hoc`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dangkyhoc`
--

LOCK TABLES `dangkyhoc` WRITE;
/*!40000 ALTER TABLE `dangkyhoc` DISABLE KEYS */;
INSERT INTO `dangkyhoc` VALUES ('faccad62493a4155bf41c25350fa9a7a','A12345','IS345','2023-1','2023-09-21 13:54:42');
/*!40000 ALTER TABLE `dangkyhoc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `monhoc`
--

DROP TABLE IF EXISTS `monhoc`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `monhoc` (
  `ma_mon_hoc` varchar(255) NOT NULL,
  `ten_mon_hoc` varchar(255) DEFAULT NULL,
  `so_tin_chi` int DEFAULT NULL,
  `he_so` float DEFAULT NULL,
  PRIMARY KEY (`ma_mon_hoc`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `monhoc`
--

LOCK TABLES `monhoc` WRITE;
/*!40000 ALTER TABLE `monhoc` DISABLE KEYS */;
INSERT INTO `monhoc` VALUES ('','Phân tích thiết kế hướng đối tượng',3,1),('	IS345','An toàn thông tin',4,1.5),('AD204','Ẩm thực Việt nam',4,2),('AD204A','Ẩm thực Việt Nam',3,2),('AD214','Nâng cao chất lượng giọng hát	AD213 (0), AD213A (1)',3,1),('AD240','Nhiếp ảnh cơ bản',3,2),('AD242','Thiết kế mĩ thuật 1',3,1),('IS345','An toàn thông tin 1',2,3),('MA110A','Giải tích 1A',4,2),('PG102','GDTC: Thể dục cổ truyền cơ bản',3,1.5);
/*!40000 ALTER TABLE `monhoc` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `mucphi`
--

DROP TABLE IF EXISTS `mucphi`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `mucphi` (
  `nam` int NOT NULL,
  `hoc_phi` float DEFAULT NULL,
  PRIMARY KEY (`nam`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `mucphi`
--

LOCK TABLES `mucphi` WRITE;
/*!40000 ALTER TABLE `mucphi` DISABLE KEYS */;
INSERT INTO `mucphi` VALUES (2023,456);
/*!40000 ALTER TABLE `mucphi` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sinhvien`
--

DROP TABLE IF EXISTS `sinhvien`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `sinhvien` (
  `ma_sv` varchar(255) NOT NULL,
  `ho_ten` varchar(255) DEFAULT NULL,
  `dia_chi` varchar(255) DEFAULT NULL,
  `ngay_sinh` varchar(255) DEFAULT NULL,
  `khoa_hoc` int DEFAULT NULL,
  PRIMARY KEY (`ma_sv`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sinhvien`
--

LOCK TABLES `sinhvien` WRITE;
/*!40000 ALTER TABLE `sinhvien` DISABLE KEYS */;
INSERT INTO `sinhvien` VALUES ('A12345','Nguyễn Văn B','456st','12/4/2004',35),('A14569','Hoàng Thị D','12 st','15/9/2006',36),('A46123','Nguyễn Văn A','123 st','12/3/2003',34),('A78945','Lê Văn C','789 st','17/5/2002',33);
/*!40000 ALTER TABLE `sinhvien` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-09-21 14:01:40
