-- Keep a log of any SQL queries you execute as you solve the mystery.

--CRIME SCENCE REPORTS ON 28TH JULY ON SPECIFIC STREET
SELECT description FROM crime_scene_reports WHERE day = 28 AND month = 7 AND year = 2023 AND street = 'Humphrey Street';

--SELECT SPECIFC INTERVIEWS FROM THAT DAY
SELECT name, transcript FROM interviews WHERE day = 28 AND month = 7 AND year = 2023;

SELECT * FROM bakery_security_logs WHERE day = 28 AND month = 7 AND year = 2023 AND activity ='exit' AND hour = 10 AND minute >= 20 ORDER BY hour ;
SELECT * FROM bakery_security_logs WHERE day = 28 AND month = 7 AND year = 2023 AND activity ='exit' AND hour = 10  ORDER BY hour ;

--GET PEOPLE NUMBER PLATES
SELECT * FROM people WHERE license_plate = '0NTHK55';

SELECT * FROM people WHERE people.phone_number = '(717) 555-1342';

--ATM THAT THE WITHDRAW TRANSACTIONS WAS MADE
SELECT * FROM atm_transactions WHERE day = 28 AND month = 7 AND year = 2023 AND atm_location = 'Leggett Street' AND transaction_type ='withdraw';

--PHONE CALLS MADE ON 28TH
SELECT * FROM phone_calls WHERE day = 28 AND month = 7 AND year = 2023 AND duration < 60 ORDER BY duration ASC;

--FIND THE PEOPLE WITH THE BANK ACCOUNTS THAT MADE WITHDRAWALS
SELECT * FROM bank_accounts JOIN people ON bank_accounts.person_id = people.id WHERE account_number = 26013199;

--CHECK FLIGHTS
SELECT * FROM flights WHERE day = 29 AND month = 7 AND year = 2023 ORDER BY hour DESC;

SELECT * FROM airports WHERE origin_airport_id = 36;

--CHECK IF THEY ARE A PASSANGER
SELECT * FROM passengers WHERE passport_number = 5773159633;

--CHECK FOR THE CITY
SELECT * FROM airports;
