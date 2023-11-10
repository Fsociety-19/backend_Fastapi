-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 10-09-2023 a las 08:18:29
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `appointmenthub`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `appointments`
--

CREATE TABLE `appointments` (
  `id` int(11) NOT NULL,
  `reason` varchar(200) NOT NULL,
  `idstudent` int(11) NOT NULL,
  `idAdminStaff` int(11) DEFAULT NULL,
  `hour` time NOT NULL DEFAULT current_timestamp(),
  `date` date NOT NULL DEFAULT current_timestamp(),
  `idStatusAppointment` int(11) NOT NULL DEFAULT 1,
  `detail` varchar(200) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `appointments`
--

INSERT INTO `appointments` (`id`, `reason`, `idstudent`, `idAdminStaff`, `hour`, `date`, `idStatusAppointment`, `detail`) VALUES
(3, 'Matricula fallida', 4, NULL, '23:41:05', '2023-09-26', 1, 'Informacion adicional-');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `detailuser`
--

CREATE TABLE `detailuser` (
  `id` int(11) NOT NULL,
  `dni` varchar(80) NOT NULL,
  `name` varchar(80) NOT NULL,
  `lastName` varchar(80) NOT NULL,
  `idUser` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `detailuser`
--

INSERT INTO `detailuser` (`id`, `dni`, `name`, `lastName`, `idUser`) VALUES
(1, '12345678901', 'John', 'Doe', 2),
(2, '23456789012', 'Jane', 'Smith', 3),
(3, '34567890123', 'Mike', 'Jackson', 4),
(4, '45678901234', 'Susan', 'Adams', 5),
(5, '56789012345', 'David', 'Wilson', 6),
(6, '67890123456', 'Lisa', 'Johnson', 7),
(7, '78901234567', 'Robert', 'Martin', 8),
(8, '89012345678', 'Emily', 'White', 9),
(9, '3333', 'fSOCIETY', 'Sanz', 10),
(11, '22233445566', 'Alice', 'Jones', 12),
(12, '33344556677', 'Ryan', 'Smith', 13),
(13, '44455667788', 'Elizabeth', 'Davis', 14);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `rol`
--

CREATE TABLE `rol` (
  `id` int(11) NOT NULL,
  `nombre` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `rol`
--

INSERT INTO `rol` (`id`, `nombre`) VALUES
(1, 'Admin'),
(2, 'Administrativo'),
(3, 'Estudiante');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `statusappointments`
--

CREATE TABLE `statusappointments` (
  `id` int(11) NOT NULL,
  `name` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `statusappointments`
--

INSERT INTO `statusappointments` (`id`, `name`) VALUES
(3, 'ATENDIDO'),
(2, 'OBSERVACION'),
(1, 'PENDIENTE');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `username` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `idRol` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `users`
--

INSERT INTO `users` (`id`, `username`, `password`, `idRol`) VALUES
(1, 'Fsociety', 'kjjdjdjdjd', 2),
(2, 'john_doe', 'p@ssw0', 3),
(3, 'jane_smith', 'qwerty12', 3),
(4, 'mike_jackson', 'p@ssword', 3),
(5, 'susan_adams', 'secure34', 3),
(6, 'david_wilson', 'abc12345', 3),
(7, 'lisa_johnson', 'letmein7', 3),
(8, 'robert_martin', 'welcome8', 3),
(9, 'emily_white', 'sunshine', 3),
(10, 'william_davis', 'iloveyou', 3),
(11, 'sarah_brown', '1a2b3c4d', 3),
(12, 'admin_user', 'admin123', 1),
(13, 'alice_jones', 'secret22', 2),
(14, 'ryan_smith', 'myp@ss11', 2),
(15, 'elizabeth_davis', 'p@ssw0rd', 2),
(16, 'AndreJs---', 'Informacion adicional-', 3),
(19, 'Andr22222', 'Informacion adicional-', 3);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `appointments`
--
ALTER TABLE `appointments`
  ADD PRIMARY KEY (`id`),
  ADD KEY `idStatusAppointment` (`idStatusAppointment`),
  ADD KEY `idAdminStaff` (`idAdminStaff`),
  ADD KEY `idstudent` (`idstudent`);

--
-- Indices de la tabla `detailuser`
--
ALTER TABLE `detailuser`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `UNIQUE` (`dni`),
  ADD UNIQUE KEY `IDUSER` (`idUser`),
  ADD UNIQUE KEY `idUser_2` (`idUser`);

--
-- Indices de la tabla `rol`
--
ALTER TABLE `rol`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `statusappointments`
--
ALTER TABLE `statusappointments`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `unique` (`name`);

--
-- Indices de la tabla `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD KEY `idRol` (`idRol`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `appointments`
--
ALTER TABLE `appointments`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=10;

--
-- AUTO_INCREMENT de la tabla `detailuser`
--
ALTER TABLE `detailuser`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT de la tabla `rol`
--
ALTER TABLE `rol`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `statusappointments`
--
ALTER TABLE `statusappointments`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;

--
-- AUTO_INCREMENT de la tabla `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=20;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `appointments`
--
ALTER TABLE `appointments`
  ADD CONSTRAINT `appointments_ibfk_3` FOREIGN KEY (`idStatusAppointment`) REFERENCES `statusappointments` (`id`),
  ADD CONSTRAINT `appointments_ibfk_4` FOREIGN KEY (`idAdminStaff`) REFERENCES `users` (`id`),
  ADD CONSTRAINT `appointments_ibfk_5` FOREIGN KEY (`idstudent`) REFERENCES `users` (`id`);

--
-- Filtros para la tabla `detailuser`
--
ALTER TABLE `detailuser`
  ADD CONSTRAINT `detailuser_ibfk_1` FOREIGN KEY (`idUser`) REFERENCES `users` (`id`);

--
-- Filtros para la tabla `users`
--
ALTER TABLE `users`
  ADD CONSTRAINT `users_ibfk_2` FOREIGN KEY (`idRol`) REFERENCES `rol` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
