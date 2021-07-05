import csv
a = [[],[],[],[],[],[],[]] #a는 [[월],[화],[수],[목],[금],[토],[일]]인 이차원 딕셔너리임.
with open('passby_data.CSV') as table: #csv파일을 읽고 그걸 table이라고 하겠다. 
  reader = csv.DictReader(table) #reader는 table을 딕셔너리로 읽는다.
  i = 0 #요일(i) 0으로 초기화 / 사실상 요일이 아니라 요일의 순서를 의미
  j = 0 #시간(j) 0으로 초기화
  for row in reader: #reader에서 row를 가져와서 모두 넣을 것이다.
    a[i].append(row) #a[i]즉 [[],[],[],[],[],[],[]] 안의 []에 가져온 row를 넣는다. 
    #그러면 전체 테이블로 딕셔너리 하나가 나옴
    j += 1 #한줄씩 내려 갈수록 시간은 1시간씩 늘어남
    if(j % 24 == 0): #만약 그 시간이 24시간이 되면
      i += 1 #요일이 하루 넘어감
x_title=['월','화','수','목','금','토','일']
for i in range(0,7):#월~일까지 7번 반복
  for j in range(0,len(a[i])):#데이터 수만큼 반복
    print(x_title[i],'[',j,']=',a[i][j])
