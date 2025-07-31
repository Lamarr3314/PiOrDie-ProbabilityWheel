CREATE DATABASE pi;
CREATE Table user_info(
    user_id INT PRIMARY KEY AUTO_INCREMENT,
    user_name VARCHAR(255) NOT NULL,
    first_score INT NOT NULL DEFAULT 0,
    second_score INT NOT NULL DEFAULT 0,
    third_score INT NOT NULL DEFAULT 0,
    total_score INT NOT NULL DEFAULT 0
)