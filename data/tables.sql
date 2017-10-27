CREATE TABLE visits (
  visitor_id CHAR(36),
  user_id INTEGER,
  country VARCHAR,
  timezone VARCHAR,
  location_accuracy INTEGER
);

CREATE TABLE reading (
  is_app_event BOOLEAN,
  visitor_id CHAR(36),
  id CHAR(36),
  visit_id CHAR(36),
  tracking_time TIMESTAMP,
  created_at TIMESTAMP,
  story_id INTEGER,
  user_id INTEGER
);

CREATE TABLE stories (
  id INTEGER,
  user_id INTEGER,
  teaser VARCHAR,
  title VARCHAR,
  cover CHAR(36),
  category_one VARCHAR(16),
  category_two VARCHAR(16)
);