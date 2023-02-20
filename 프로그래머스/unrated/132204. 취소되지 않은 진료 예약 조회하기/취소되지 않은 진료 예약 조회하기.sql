SELECT
a1.APNT_NO
, a3.PT_NAME
, a3.PT_No
, a2.MCDP_CD
, a2.DR_NAME
, a1.APNT_YMD
from APPOINTMENT a1
left outer join DOCTOR a2 on a1.MDDR_ID = a2.DR_ID
left outer join PATIENT a3 on a1.PT_NO = a3.PT_NO
where a1.APNT_CNCL_YN = 'N'
and date(a1.APNT_YMD) = '2022-04-13'
and a2.MCDP_CD = 'CS'
order by a1.APNT_YMD