#!/usr/bin/python3
import openpyxl
wb = openpyxl.load_workbook( "student.xlsx" )
ws = wb['Sheet1']
row_id = 1
for row in ws:
	if row_id != 1:
		sum_v = ws.cell(row = row_id, column = 3).value * 0.3
		sum_v += ws.cell(row = row_id, column = 4).value * 0.35
		sum_v += ws.cell(row = row_id, column = 5).value * 0.34
		sum_v += ws.cell(row = row_id, column = 6).value
		ws.cell(row = row_id, column = 7).value = sum_v
	row_id += 1
# grade
score = []
for row in ws:
	score.append(row[6].value)
del score[0]
score.sort()
row_id = 1
for row in ws:
	if row_id != 1:
		total_score = ws.cell(row = row_id, column = 7).value
		if total_score <= score[round(len(score) * 0.3)]:
			if total_score <= score[round(len(score) * 0.15)]:
				ws.cell(row = row_id, column = 8).value = 'C0'
			else:
				ws.cell(row = row_id, column = 8).value = 'C+'
		elif total_score <= score[round(len(score) * 0.7)]:
			if total_score <= score[round(len(score) * 0.5)]:
				ws.cell(row = row_id, column = 8).value = 'B0'
			else:
				ws.cell(row = row_id, column = 8).value = 'B+'
		else:
			if total_score <= score[round(len(score) * 0.85)]:
				ws.cell(row = row_id, column = 8).value = 'A0'
			else:
				ws.cell(row = row_id, column = 8).value = 'A+'
	row_id += 1
wb.save( "student.xlsx" )
