-- 코드를 입력하세요
SELECT I.NAME, I.DATETIME
FROM ANIMAL_INS I
left join ANIMAL_OUTS O
on I.ANIMAL_ID = O.ANIMAL_ID
where O.ANIMAL_ID is null
order by I.DATETIME
limit 3;