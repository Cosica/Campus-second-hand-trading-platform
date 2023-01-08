/*
 Navicat Premium Data Transfer

 Source Server         : MySQL
 Source Server Type    : MySQL
 Source Server Version : 80017
 Source Host           : localhost:3306
 Source Schema         : trade

 Target Server Type    : MySQL
 Target Server Version : 80017
 File Encoding         : 65001

 Date: 27/06/2020 03:26:22
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for goods
-- ----------------------------
DROP TABLE IF EXISTS `goods`;
CREATE TABLE `goods`  (
  `Seller` char(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Gno` char(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Gname` char(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Price` float NOT NULL,
  `Num` int(11) NOT NULL,
  PRIMARY KEY (`Gno`) USING BTREE,
  INDEX `Seller`(`Seller`) USING BTREE,
  CONSTRAINT `goods_ibfk_1` FOREIGN KEY (`Seller`) REFERENCES `user` (`Uname`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of goods
-- ----------------------------
INSERT INTO `goods` VALUES ('Sekiro', '#goods1', '电风扇', 80, 0);
INSERT INTO `goods` VALUES ('Sekiro', '#goods2', '电瓶车', 1800, 0);
INSERT INTO `goods` VALUES ('Sekiro', '#goods3', '暖水壶', 40, 5);
INSERT INTO `goods` VALUES ('Sekiro', '#goods4', '热水袋', 20, 15);
INSERT INTO `goods` VALUES ('Sekiro', '#goods5', '水果刀', 10, 30);
INSERT INTO `goods` VALUES ('八方旅人', '#mine-1', '电风扇', 60, 9);
INSERT INTO `goods` VALUES ('八方旅人', '#mine-2', '床上桌', 120, 0);
INSERT INTO `goods` VALUES ('八方旅人', '#mine-3', '电脑', 800, 1);
INSERT INTO `goods` VALUES ('八方旅人', '#mine-4', 'ps4', 1200, 1);
INSERT INTO `goods` VALUES ('八方旅人', '#mine-5', '晾衣架', 90, 3);
INSERT INTO `goods` VALUES ('Smile', 'haha-1', '电子手表', 50.7, 4);
INSERT INTO `goods` VALUES ('Smile', 'haha-2', '衣服撑子', 5, 10);
INSERT INTO `goods` VALUES ('Smile', 'haha-3', '工图筒', 10, 8);
INSERT INTO `goods` VALUES ('Smile', 'haha-4', '绘图工具', 20, 3);
INSERT INTO `goods` VALUES ('张方耀', 'my-1', '手机', 400, 3);
INSERT INTO `goods` VALUES ('张方耀', 'my-2', '自行车', 200, 3);
INSERT INTO `goods` VALUES ('张方耀', 'my-3', '水桶', 20, 9);
INSERT INTO `goods` VALUES ('张方耀', 'my-4', '计算器', 90, 6);
INSERT INTO `goods` VALUES ('张方耀', 'my-5', '洗脸盆', 12.8, 6);
INSERT INTO `goods` VALUES ('Smile', 'plex-5', '充电宝', 20, 1);

-- ----------------------------
-- Table structure for orders
-- ----------------------------
DROP TABLE IF EXISTS `orders`;
CREATE TABLE `orders`  (
  `Buyer` char(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Seller` char(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Gno` char(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Gname` char(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Address` char(80) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Quantity` int(11) NOT NULL,
  `Cost` float NOT NULL,
  INDEX `Buyer`(`Buyer`) USING BTREE,
  INDEX `Seller`(`Seller`) USING BTREE,
  INDEX `Gno`(`Gno`) USING BTREE,
  CONSTRAINT `orders_ibfk_1` FOREIGN KEY (`Buyer`) REFERENCES `user` (`Uname`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `orders_ibfk_2` FOREIGN KEY (`Seller`) REFERENCES `goods` (`Seller`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `orders_ibfk_3` FOREIGN KEY (`Gno`) REFERENCES `goods` (`Gno`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of orders
-- ----------------------------
INSERT INTO `orders` VALUES ('shuiahiua', '八方旅人', '#mine-2', '床上桌', 'sdds', 3, 360);
INSERT INTO `orders` VALUES ('shuiahiua', 'Sekiro', '#goods3', '暖水壶', 'asdad', 1, 40);
INSERT INTO `orders` VALUES ('shuiahiua', 'Sekiro', '#goods1', '电风扇', '1', 1, 80);
INSERT INTO `orders` VALUES ('1', 'Sekiro', '#goods1', '电风扇', '3', 3, 240);
INSERT INTO `orders` VALUES ('Smile', 'Sekiro', '#goods3', '暖水壶', '哈尔滨工程大学', 2, 80);
INSERT INTO `orders` VALUES ('Smile', 'Sekiro', '#goods4', '热水袋', '哈尔滨工程大学', 5, 100);

-- ----------------------------
-- Table structure for user
-- ----------------------------
DROP TABLE IF EXISTS `user`;
CREATE TABLE `user`  (
  `Uid` char(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Uname` char(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Password` char(40) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Admin` char(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  PRIMARY KEY (`Uname`) USING BTREE,
  UNIQUE INDEX `Uid`(`Uid`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of user
-- ----------------------------
INSERT INTO `user` VALUES ('1', '1', '1', '0');
INSERT INTO `user` VALUES ('Admin', 'Alex', '147852963', '1');
INSERT INTO `user` VALUES ('1075791841', 'Sekiro', 'qq123', '1');
INSERT INTO `user` VALUES ('12058464', 'shuiahiua', '123', '1');
INSERT INTO `user` VALUES ('3293285267', 'Smile', '123456789', '0');
INSERT INTO `user` VALUES ('65165112', '不爱我就拉岛', 'asdfg', '0');
INSERT INTO `user` VALUES ('1323864184', '八方旅人', 'qwertyu123456', '0');
INSERT INTO `user` VALUES ('16512315', '张方耀', 'zxcvb', '0');

-- ----------------------------
-- Table structure for wishlist
-- ----------------------------
DROP TABLE IF EXISTS `wishlist`;
CREATE TABLE `wishlist`  (
  `Uname` char(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Seller` char(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Gno` char(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Gname` char(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NOT NULL,
  `Price` float NOT NULL,
  INDEX `Uname`(`Uname`) USING BTREE,
  INDEX `Gno`(`Gno`) USING BTREE,
  CONSTRAINT `wishlist_ibfk_1` FOREIGN KEY (`Uname`) REFERENCES `user` (`Uname`) ON DELETE RESTRICT ON UPDATE RESTRICT,
  CONSTRAINT `wishlist_ibfk_2` FOREIGN KEY (`Gno`) REFERENCES `goods` (`Gno`) ON DELETE RESTRICT ON UPDATE RESTRICT
) ENGINE = InnoDB CHARACTER SET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of wishlist
-- ----------------------------
INSERT INTO `wishlist` VALUES ('Smile', 'Sekiro', '#goods1', '电风扇', 80);
INSERT INTO `wishlist` VALUES ('Smile', '八方旅人', '#mine-1', '电风扇', 60);
INSERT INTO `wishlist` VALUES ('Smile', '八方旅人', '#mine-4', 'ps4', 1200);
INSERT INTO `wishlist` VALUES ('Smile', '张方耀', 'my-1', '手机', 400);
INSERT INTO `wishlist` VALUES ('Smile', '张方耀', 'my-2', '自行车', 200);

SET FOREIGN_KEY_CHECKS = 1;
