-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Oct 12, 2022 at 09:51 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hotel`
--

-- --------------------------------------------------------

--
-- Table structure for table `feedback`
--

CREATE TABLE `feedback` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `description` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- --------------------------------------------------------

--
-- Table structure for table `register`
--

CREATE TABLE `register` (
  `username` varchar(20) DEFAULT NULL,
  `email` varchar(20) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `register`
--

INSERT INTO `register` (`username`, `email`, `password`) VALUES
('anurag', 'anuragshinde@gmail.c', 'Anurag01@'),
('vishal', 'vishal@gmail.com', 'vishal01'),
('rajul', 'rajul@gmail.com', 'rajul01@'),
('Anurag', 'anuragshinde@gmail.c', 'anurag01@'),
('anurag', 'anuragshinde@gmail.c', 'anurag786'),
('anurag', 'anurag@gmail.com', 'Anurag01'),
('sumit', 'sumit@gmail.com', 'sumit1234'),
('rajul', 'rajul@gmail.com', 'rajul1234'),
('anurag', 'anuragshinde@gmail.c', 'anurag1234'),
('anurag', 'anuragshinde@gmail.c', 'anurag7907'),
('avinash', 'avinash@gmail.com', 'Avinash1244'),
('Omkar Patil', 'omkar@gmail.com', 'omkar1234'),
('mahesh', 'mahesh@gmail.com', 'mahesh1234'),
('swarup', 'swarup@gmail.com', 'swarup1234'),
('mihir', 'mihir@gmail.com', 'mihir1234'),
('shri', 'shri@gmail.com', 'shri1234'),
('anurag', 'anurag01@gmail.com', 'anurag123');

-- --------------------------------------------------------

--
-- Table structure for table `registeruser`
--

CREATE TABLE `registeruser` (
  `uid` int(11) NOT NULL,
  `name` varchar(20) DEFAULT NULL,
  `email` varchar(20) DEFAULT NULL,
  `phoneno` int(11) DEFAULT NULL,
  `gender` varchar(20) DEFAULT NULL,
  `roomno` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `registeruser`
--

INSERT INTO `registeruser` (`uid`, `name`, `email`, `phoneno`, `gender`, `roomno`) VALUES
(11, 'shri', 'shri@gmail.com', 980277192, 'male', 102);

-- --------------------------------------------------------

--
-- Table structure for table `room`
--

CREATE TABLE `room` (
  `roomno` int(11) DEFAULT NULL,
  `Availability` varchar(20) DEFAULT NULL,
  `status` varchar(20) DEFAULT NULL,
  `bedtype` varchar(20) DEFAULT NULL,
  `price` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `room`
--

INSERT INTO `room` (`roomno`, `Availability`, `status`, `bedtype`, `price`) VALUES
(101, 'Available', 'cleaned', 'single bed', 1000);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `feedback`
--
ALTER TABLE `feedback`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `registeruser`
--
ALTER TABLE `registeruser`
  ADD PRIMARY KEY (`uid`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `feedback`
--
ALTER TABLE `feedback`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=7;

--
-- AUTO_INCREMENT for table `registeruser`
--
ALTER TABLE `registeruser`
  MODIFY `uid` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
