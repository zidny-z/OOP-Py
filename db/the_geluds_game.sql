-- phpMyAdmin SQL Dump
-- version 5.0.4
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Dec 31, 2020 at 07:43 PM
-- Server version: 10.4.17-MariaDB
-- PHP Version: 8.0.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `the geluds game`
--

-- --------------------------------------------------------

--
-- Table structure for table `enemy`
--

CREATE TABLE `enemy` (
  `EnemyID` int(11) NOT NULL,
  `EnemyName` varchar(20) NOT NULL,
  `EnemyHealth` int(11) NOT NULL,
  `EnemyLevel` int(11) NOT NULL,
  `EnemyPower` int(11) NOT NULL,
  `EnemyArmor` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `enemy`
--

INSERT INTO `enemy` (`EnemyID`, `EnemyName`, `EnemyHealth`, `EnemyLevel`, `EnemyPower`, `EnemyArmor`) VALUES
(1, 'Munos', 150, 1, 6, 8),
(2, 'Zedos', 200, 2, 8, 7),
(3, 'Dosan', 250, 3, 10, 8),
(4, 'Zaoshi', 300, 4, 12, 11),
(5, 'Zugo', 400, 5, 15, 12),
(6, 'Euriale', 450, 6, 18, 20),
(7, 'Ofiotaur', 500, 7, 21, 19),
(8, 'Talos', 650, 8, 23, 25),
(9, 'Stheno', 800, 9, 28, 31),
(10, 'Gerion', 1000, 10, 30, 32);

-- --------------------------------------------------------

--
-- Table structure for table `hero`
--

CREATE TABLE `hero` (
  `HeroID` int(11) NOT NULL,
  `HeroName` varchar(20) NOT NULL,
  `HeroHealth` int(11) NOT NULL,
  `HeroPower` int(11) NOT NULL,
  `HeroArmor` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `hero`
--

INSERT INTO `hero` (`HeroID`, `HeroName`, `HeroHealth`, `HeroPower`, `HeroArmor`) VALUES
(1, 'Kalibur', 175, 20, 18),
(2, 'Shin', 175, 19, 21),
(3, 'Dranton', 175, 18, 22),
(4, 'Darius', 175, 23, 19),
(5, 'Earl', 175, 21, 24);

-- --------------------------------------------------------

--
-- Table structure for table `player`
--

CREATE TABLE `player` (
  `PlayeraID` int(11) NOT NULL,
  `PlayerName` varchar(20) NOT NULL,
  `PlayerHealth` int(11) NOT NULL DEFAULT 100,
  `PlayerEXP` int(11) NOT NULL DEFAULT 0,
  `PlayerLevel` int(11) NOT NULL DEFAULT 1,
  `PlayerHero` int(11) NOT NULL,
  `PlayerWeapon` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `weapon`
--

CREATE TABLE `weapon` (
  `WeaponID` int(11) NOT NULL,
  `WeaponName` varchar(20) NOT NULL,
  `WeaponPower` int(11) NOT NULL,
  `CritRate` int(11) NOT NULL,
  `CritDamage` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `weapon`
--

INSERT INTO `weapon` (`WeaponID`, `WeaponName`, `WeaponPower`, `CritRate`, `CritDamage`) VALUES
(1, 'Sword', 22, 19, 14),
(2, 'Bow', 19, 16, 13),
(3, 'Hammer', 23, 18, 21),
(4, 'Knuckle', 16, 11, 13),
(5, 'Axe', 20, 18, 15),
(6, 'Nunchaku', 17, 12, 15),
(7, 'Toya', 18, 15, 16),
(8, 'Katar', 21, 17, 16),
(9, 'Spear', 15, 20, 18),
(10, 'Halberd', 20, 15, 17);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `enemy`
--
ALTER TABLE `enemy`
  ADD PRIMARY KEY (`EnemyID`);

--
-- Indexes for table `hero`
--
ALTER TABLE `hero`
  ADD PRIMARY KEY (`HeroID`);

--
-- Indexes for table `player`
--
ALTER TABLE `player`
  ADD PRIMARY KEY (`PlayeraID`),
  ADD KEY `PlayerHero` (`PlayerHero`),
  ADD KEY `PlayerWeapon` (`PlayerWeapon`);

--
-- Indexes for table `weapon`
--
ALTER TABLE `weapon`
  ADD PRIMARY KEY (`WeaponID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `hero`
--
ALTER TABLE `hero`
  MODIFY `HeroID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `player`
--
ALTER TABLE `player`
  MODIFY `PlayeraID` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `weapon`
--
ALTER TABLE `weapon`
  MODIFY `WeaponID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `player`
--
ALTER TABLE `player`
  ADD CONSTRAINT `player_ibfk_1` FOREIGN KEY (`PlayerHero`) REFERENCES `hero` (`HeroID`),
  ADD CONSTRAINT `player_ibfk_2` FOREIGN KEY (`PlayerWeapon`) REFERENCES `weapon` (`WeaponID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
