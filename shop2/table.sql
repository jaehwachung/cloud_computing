CREATE TABLE shop_member (
	id INTEGER NOT NULL IDENTITY(1,1), 
	name VARCHAR(50) NULL, 
	email VARCHAR(200) NULL, 
	password VARCHAR(32) NULL, 
	post_code VARCHAR(5) NULL, 
	address VARCHAR(255) NULL, 
	detail_address VARCHAR(255) NULL, 
	is_admin CHAR(1) NULL, 
	create_date DATETIME NULL, 
	PRIMARY KEY (id), 
	UNIQUE (email)
)

CREATE TABLE goods (
	id INTEGER NOT NULL IDENTITY(1,1), 
	goods_name VARCHAR(255) NULL, 
	price INTEGER NULL, 
	goods_photo VARCHAR(255) NULL, 
	goods_cnt INTEGER NULL, 
	goods_ranking INTEGER NULL, 
	goods_description VARCHAR(max) NULL, 
	PRIMARY KEY (id)
)

CREATE TABLE orders (
	id INTEGER NOT NULL IDENTITY(1,1), 
	order_str_id VARCHAR(100) NULL, 
	member INTEGER NULL, 
	order_date DATETIME NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(member) REFERENCES shop_member (id)
)

CREATE TABLE orders_item (
	id INTEGER NOT NULL IDENTITY(1,1), 
	goods INTEGER NULL, 
	goods_price INTEGER NULL, 
	goods_cnt INTEGER NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(goods) REFERENCES goods (id)
)

CREATE TABLE basket (
	id INTEGER NOT NULL IDENTITY(1,1), 
	member INTEGER NULL, 
	goods INTEGER NULL, 
	goods_cnt INTEGER NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(member) REFERENCES shop_member (id), 
	FOREIGN KEY(goods) REFERENCES goods (id)
)

CREATE TABLE goods_tracking (
	id INTEGER NOT NULL IDENTITY(1,1), 
	order_id INTEGER NULL, 
	delivery_start_date DATETIME NULL, 
	delivery_end_date DATETIME NULL, 
	tracking_number VARCHAR(50) NULL, 
	tracking_status VARCHAR(30) NULL, 
	PRIMARY KEY (id), 
	FOREIGN KEY(order_id) REFERENCES orders (id)
)