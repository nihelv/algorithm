-- 코드를 입력하세요
SELECT O.ANIMAL_ID, O.ANIMAL_TYPE, O.NAME
FROM ANIMAL_OUTS O 
inner join ANIMAL_INS I
on I.ANIMAL_ID = O.ANIMAL_ID
where I.SEX_UPON_INTAKE != O.SEX_UPON_OUTCOME;
