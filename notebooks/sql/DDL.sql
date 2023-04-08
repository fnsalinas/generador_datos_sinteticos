DROP TABLE IF EXISTS gcp_poc.onpremise.clients;
CREATE TABLE gcp_poc.onpremise.clients (
  customer_id varchar, --93C1B476399A4811831DDBAAA6663260
  nif varchar, --98393511V
  first_name varchar, --Carla
  last_name varchar, --Valencia
  date_of_birth date, --1916-05-22
  sex varchar, --female
  blood_group varchar, --B+
  city varchar, --Ourense
  customer_address varchar, --Alameda Nicanor Serra 970 Apt. 78 Huelva, 31902
  lat float, --89.4079935
  long float, --27.273604
  region varchar, --Cataluña
  timezone varchar, --Indian/Mauritius
  customer_phone varchar, --+34949 023 349
  customer_email varchar, --lralevanln_992@gmail.com
  customer_created_at timestamp, --2021-06-11 04:02:31 UTC
  customer_updated_at timestamp --
);

DROP TABLE IF EXISTS gcp_poc.onpremise.users;
CREATE TABLE gcp_poc.onpremise.users (
  user_id varchar, --98A1423B2E5A435899D7480081F4218D
  customer_id varchar, --93C1B476399A4811831DDBAAA6663260
  user_name varchar, --carla_valencia_5661
  user_password varchar, --tN^4Ph^tZ#
  user_email varchar, --lralevanln_992@gmail.com
  user_phone varchar, --+34949 023 349
  user_image_url varchar, --https://placekitten.com/419/935
  url varchar, --https://www.silva.com/
  user_created_at timestamp, --2021-06-11 04:02:31 UTC
  user_updated_at timestamp --
);

DROP TABLE IF EXISTS gcp_poc.onpremise.products;
CREATE TABLE gcp_poc.onpremise.products (
  product_id varchar, --5631011466BD40C2BB538B518A78FE2A
  product_name varchar, --Zanahoria (Kg.)
  product_description varchar, --Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s  when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries  but also the leap into electronic typesetting  remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages  and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
  product_price numeric, --4803
  product_category varchar, --Frutas y Verduras
  product_stock integer, --1771
  product_rating integer, --1
  product_rating_count integer, --62773
  product_reviews_count integer, --286
  product_reviews varchar, --
  product_tags varchar, --Productos de frutas y verduras
  product_created_at timestamp, --2000-01-01 12:00:00 UTC
  product_updated_at timestamp --2005-04-07 14:25:00 UTC
);

DROP TABLE IF EXISTS gcp_poc.onpremise.categories;
CREATE TABLE gcp_poc.onpremise.categories (
  category_id varchar, --7A706060E0164B97BC65E0AA4660E3EE
  category_name varchar, --Frutas y Verduras
  category_description varchar, --Lorem Ipsum is simply dummy text of the 
  category_image_url varchar, --https://placekitten.com/819/150
  category_created_at timestamp, --2000-01-01 12:00:00 UTC
  category_updated_at timestamp --
);

DROP TABLE IF EXISTS gcp_poc.onpremise.orders;
CREATE TABLE gcp_poc.onpremise.orders (
  order_id varchar, --E3CA997E7BD64583B8897C73ADCF9EE9
  order_customer_id varchar, --93C1B476399A4811831DDBAAA6663260
  order_product_id varchar, --5631011466BD40C2BB538B518A78FE2A
  order_quantity int, --3
  order_price numeric, --4803
  order_created_at timestamp, --2022-03-21 03:06:13 UTC
  order_updated_at timestamp --
);

DROP TABLE IF EXISTS gcp_poc.onpremise.invoices;
CREATE TABLE gcp_poc.onpremise.invoices (
  invoice_id varchar, --257E65DDFECE4C139CC0B4B0EC0B8A12
  invoice_customer_id varchar, --93C1B476399A4811831DDBAAA6663260
  invoice_order_id varchar, --E3CA997E7BD64583B8897C73ADCF9EE9
  invoice_amount numeric, --14409.0
  invoice_created_at timestamp, --2023-03-31 02:50:15 UTC
  invoice_updated_at timestamp --
);