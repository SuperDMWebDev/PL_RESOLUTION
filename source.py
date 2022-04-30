import os
import numpy as np
from pyparsing import alphas
def checkTwoOpposite(string1,string2):
   if string1 == "-"+string2 or "-"+string1==string2:
      return True
   return False
def sortArray(array):
   if array!=[]:
      if len(array[0])==2:
         if array[0][0]!= '-':
            array[0].sort()
def sortBigArray(array):
   if len(array) == 2:
      array.sort()
def pl_resolve(C1, C2):
    res = []
    k=False
    # Duyệt từng câu trong C1
    for i in range(len(C1)):
        # Kiểm tra có câu đối trong C2 hay không -> Có -> thực hiện hợp giải
      for j in range(len(C2)):
            if(checkTwoOpposite(C1[i],C2[j])):
               k=True
               # Sao chép sang một mệnh đề tạm
               temp1= C1.copy()
               temp2 = C2.copy()

               # Xóa câu và câu đối khỏi mệnh đề tương ứng
               temp1.pop(i)
               temp2.pop(j)

               # Hợp hai mệnh đề
               resTemp=temp1 + temp2


              
            
               # Những mệnh đề luôn đúng được loại bỏ
               if(len(resTemp)==0):
                  print("Khong co")
               elif(len(resTemp)==1):
                  res.append(resTemp[0])
               elif(len(resTemp)==2):
                  if not checkTwoOpposite(resTemp[0],resTemp[1]):
                     res.append(resTemp)
                  else:
                     k=False
               #len(resTem>3)
               else:
                  res.append(resTemp)
                # Sắp xếp theo thứ tự bảng chữ cái
               sortArray(res)
    if res!=[]:
      res[0]=list(dict.fromkeys(res[0]))
    return res,k

def AddToArray(array1,array2):
   k=array2 in array1
   return k
 
def pl_resolution(KB, alpha):
    # Sao chép Knowledge Base
   clauses = KB.copy()     


   NegativeClauseAlpha=negativeClause(alpha);
   if len(NegativeClauseAlpha)>=2:
      for i in range(len(NegativeClauseAlpha)):
         KB1=[]
         KB1.append(NegativeClauseAlpha[i])
         clauses.append(KB1)
   else:
      clauses.append(NegativeClauseAlpha);
    # Thêm đối của alpha
    
    # Kết quả mỗi lần thực hiện vòng lặp
   result = []             
   for i in range(len(clauses) - 1):
         sortBigArray(clauses[i])
   while True:
         new=[]                   # Danh sách mệnh đề chứa kết quả thực hiện sau khi duyệt từ Ci, Cj
         for i in range(len(clauses) - 1):
            Ci = clauses[i]
            for j in range(i + 1, len(clauses)):
                Cj = clauses[j]
                resolvents,k = pl_resolve(Ci, Cj)     # Hợp giải Ci, Cj
                if resolvents!=[] or k==True:
                  if AddToArray(new,resolvents)==False:
                     new.append(resolvents)      # Thêm kết quả hợp giải vào new
        
         new= np.ravel(new)
         newArr=[]
         for i in range(len(new)):
            newArr.append(np.ravel(new[i]))
         newArr1=[]
         for i in range(len(newArr)):
            tempArr=[]
            for j in range(len(newArr[i])):
               tempArr.append(newArr[i][j])
            newArr1.append(tempArr)
         print(newArr1)   
         #newArr1 la new

         #newArr1-clauses
         #result1 la new bi tru
         for i in range(len(newArr1) - 1):
            sortBigArray(newArr1[i])
         result1 = [a for a  in newArr1 if a not in clauses]
         result.append(result1)  
         print(result)
                     #do nothing
                
                               # Lưu lại kết quả của lần lặp này

         for i in range(len(newArr1)):
            if (len(newArr1[i])==0):          # Nếu tồn tại mệnh đề rỗng thì trả về đúng 
                return True, result                 # và kết quả mỗi lần lặp đã thực hiện được

         if len(result1)==0:               # Nếu kết quả quả lần lặp này là con của clauses thì trả về sai 
            return False, result                    # và kết quả mỗi lần lặp đã thực hiện được
         for i in range(len(result1)):
            clauses.append(result1[i])
         print(clauses)


def negativeClause(clause1):
   i=0
   newClause=""
   clause = clause1.copy();
   while i < len(clause):

      #phu dinh -> khangdinh
      if(len(clause[i]) == 2):
         newClause=clause[i][1]
         clause[i] = newClause
      elif(len(clause[i])==1):
         newClause = '-'+clause[i][0];
         clause[i]= newClause;
      i+=1
   return clause;
def getLiterals(lineStr):
    alpha = []
    i = 0
    while i < len(lineStr):
        literal = lineStr[i]
        flag = False
        # - lay luon -P
        if literal == '-':
            literal += lineStr[i+1]
            i += 1
        #khoang trang,\n bo qua
        elif literal == ' ' or literal == '\n':
            flag = True
        #OR bo qua
        elif literal == 'O':
            if i < len(lineStr) - 1:
                if lineStr[i+1] == 'R':
                    flag = True
                    i += 1

        if flag == False:
            alpha.append(literal)
        i += 1

    return alpha
import os
def writeFile(resultKey,result):
   cwd = os.path.dirname(os.path.realpath(__file__))
   linkOutput = cwd + "\output";
   output_file_name=os.listdir(linkOutput);
   FinalOutput=linkOutput+"\\"+"output05.txt";
   file=open(FinalOutput,"w");
   for i in range(len(result)):
      k=True
      for j in range(len(result[i])):
         if k==True:
            k=False
            file.write(str(len(result[i]))+"\n")
         if len(result[i][j])==0:
            file.write("{}"+"\n")
         elif len(result[i][j])==1:
            file.write(result[i][j][0]+"\n")
         elif len(result[i][j])==2:
            file.write(result[i][j][0]+" OR "+result[i][j][1]+"\n")
         else:
            t=True
            for u in range(len(result[i][j])):
               if t==True:
                  t=False
                  file.write(result[i][j][0])
               else:
                  file.write(" OR "+result[i][j][u])
            file.write("\n")
   if resultKey:
        file.write('YES')
   else:
        file.write('NO')
   file.close()

def readFile():
      cwd = os.path.dirname(os.path.realpath(__file__))
      linkInput=cwd+"\input";
#    print(linkInput);
      input_file_name = os.listdir(linkInput);
#    print(input_file_name)
   # for i in range(len(input_file_name)):
      # dung input1.txt
      FinalInput=linkInput+"\\"+"input05.txt";
      print(FinalInput)
      file = open(FinalInput, 'r');
      clauseAlpha = file.readline()
        # bo di \n cua clauseAlpha
      if clauseAlpha[len(clauseAlpha)-1]=='\n':
         clauseAlpha = clauseAlpha[:-1]
        
      quantity= int(file.readline());
   
      KB = []
      KBTemp = []
      for i in range(0,quantity,1):
         # print(i)
         clause=file.readline()
         if clause[len(clause)-1]=='\n':
            clause = clause[:-1]
         KBTemp.append(clause)
      for i in range(len(KBTemp)):
         KB.append(getLiterals(KBTemp[i]))
      alphaSplit = getLiterals(clauseAlpha)
      

      #truyen kb va alpha
      result, result1= pl_resolution(KB,alphaSplit);
      print(result1)
      writeFile(result,result1)

def main():
    readFile()


main()