use chrono::{DateTime, Local};

pub struct Account<'a, Tz : chrono::TimeZone> {
    name: String,
    composition: &'a [Composition],
    creation: Option<DateTime<Tz>>,
}

pub struct Future<Tz : chrono::TimeZone> {
    name: String,
    maturity_in_months: u16,
    date: DateTime<Tz>,
}

pub struct Investment {
    name: String,
    expected_return: f32
}

pub struct Composition {
    investment: Investment,
    percentage: f32
}
