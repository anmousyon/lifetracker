create table if not exists lights (
    active integer
    time_stamp integer
)

create table if not exists nest (
    target_temp integer
    inside_temp integer
    time_stamp integer
)

create table if not exists windows (
    open integer
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
    speed integer
    odometer integer
    fuel_gauge integer
    target_temp integer
    windows_open integer
    time_stamp integer
)

create table if not exists bank (
    savings integer
    spent integer
    time_stamp integer
)

create table if not exists fit (
    steps integer
    time_stamp integer
)