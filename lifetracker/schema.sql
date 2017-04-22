create table if not exists nest (
    target_temp integer
    inside_temp integer
    time_stamp integer
)

create table if not exists water (
    amount_used integer
    time_stamp integer
)

create table if not exists electricity (
    amount_used integer
    time_stamp integer
)

create table if not exists weather (
    temperature integer
    precipitating boolean
    time_stamp integer
)

create table if not exists car (
    distance integer
    fuel_gauge integer
    temperature integer
    windows_open integer
    time_stamp integer
)

create table if not exists transamerica (
    savings integer
    time_stamp integer
)

create table if not exists google_fit (
    steps integer
    time_stamp integer
)