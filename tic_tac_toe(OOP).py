import random

class Tic_tac_toe:
    def __init__(self,table,choices):
        
        self.table=table
        self.choices=choices

    def  put_up(self,choose,shape):
        index_row=0
        finish=0
        for i in self.table:
            if finish==1:
                break
            index_column=0
            for j in i:
                if j==self.choose:
                    self.table[index_row][index_column]=shape
                    self.choices.remove(self.choose)
                    finish=1
                    break
                index_column+=1
            index_row+=1    
    def show_table(self):
        for i in self.table:
            row=''
            for j in i:
                row+=j+'|'
            print(row)
    def conclusion(self):
        index=0
        column1=''
        column2=''
        column3=''
        cross1=''
        cross2=''
        
        for i in self.table:
            row=''
            cross1+=self.table[index][index]
            cross2+=self.table[index][2-index]
            column1+=self.table[index][0]
            column2+=self.table[index][1]
            column3+=self.table[index][2]
            for j in i:
                row+=j
            index+=1    
            if row=='OOO' or row=='XXX':
                return row
                break
            elif cross1=='OOO' or cross1=='XXX':
                return cross1
                break                
                
            elif cross2=='OOO' or cross2=='XXX':
                return cross2
                break                    
                
            elif column1=='OOO' or column1=='XXX':
                
                return column1
                break
            elif column2=='OOO' or column2=='XXX':
                
                return column2
                break

            elif column3=='OOO' or column3=='XXX':
                
                return column3
                break
        else:
            if self.choices==[]:
                return 'Tie'
                
            
if __name__=='__main__':
    
            

 opponents=[]
 winners=[]
 losers=[]
 draws=[]

 human_wins=0
 cpu_wins=0
 draw=0


 open=True
 while open:
    choices=['1','2','3','4','5','6','7','8','9']
    table=[['1','2','3'],['4','5','6'],['7','8','9']]
    t1=Tic_tac_toe(table,choices)
    
    
    print('1.play with cpu')
    print('2.play with human')
    print('3.About game')
    print('4.Result_1')
    print('5.Result_2')
    print('6.Exit')
    choose=input('Choose the action:')
    if choose=='1':

                
        
        
        
        
        
        while True:
            
            choose=input('choose the shape that you want(O/X):')
            if choose.upper()=='O':
                 print('Human shape:O')
                 print('Cpu shape:X')                
                
                
                
                 while True:
                     t1.show_table()

                     print('Your turn')              
                     t1.choose=input('Choose the place:')
                     if t1.choose in t1.choices:
                         t1.put_up(t1.choose,'O')
                     

                     else:
                         print('Try again!')
                         continue
                     t1.conclusion()
                     if t1.conclusion()=='OOO':
                         t1.show_table()
                         print('You won!')
                         human_wins+=1
                         break
                     elif t1.conclusion()=='XXX':
                         t1.show_table()
                         print('Cpu won!')
                         cpu_wins+=1
                         break
                     elif t1.conclusion()=='Tie':
                         t1.show_table()
                         print('Tie')
                         draw+=1
                         break
                            


                                                
                         
                         
                                                    
                     print('Cpu turn')
                     t1.choose=random.choice(t1.choices)
                     t1.put_up(t1.choose,'X')

                     t1.conclusion()
                     if t1.conclusion()=='OOO':
                         t1.show_table()
                         print('You won!')
                         human_wins+=1
                         break
                     elif t1.conclusion()=='XXX':
                         t1.show_table()
                         print('Cpu won!')
                         cpu_wins+=1
                         break
                     elif t1.conclusion()=='Tie':
                         t1.show_table()
                         print('Tie')
                         draw+=1
                         break
                            





                 break                          
                     
                     
                     
            elif choose.upper()=='X':
                 print('Human shape:X')
                 print('Cpu shape:O')                   
                 
                 while True:
                     t1.show_table()

                     print('Your turn')
                     t1.choose=input('Choose the place:')
                     if t1.choose in t1.choices:
                         t1.put_up(t1.choose,'X')
                     

                     else:
                         print('Try again!')
                         continue
                     
                     t1.conclusion()
                     if t1.conclusion()=='OOO':
                         t1.show_table()
                         print('Cpu won!')
                         cpu_wins+=1
                         break
                     elif t1.conclusion()=='XXX':
                         t1.show_table()
                         print('You won!')
                         human_wins+=1
                         break
                     elif t1.conclusion()=='Tie':
                         t1.show_table()
                         print('Tie')
                         draw+=1
                         break
                            


                                                
                         
                         
                                                    
                     print('Cpu turn')
                     t1.choose=random.choice(t1.choices)
                     t1.put_up(t1.choose,'O')



                     t1.conclusion()
                     if t1.conclusion()=='OOO':
                         t1.show_table()
                         print('Cpu won!')
                         cpu_wins+=1
                         break
                     elif t1.conclusion()=='XXX':
                         t1.show_table()
                         print('You won!')
                         human_wins+=1
                         break
                     elif t1.conclusion()=='Tie':
                         t1.show_table()
                         print('Tie')
                         draw+=1
                         break
                            




                     

                 break                   
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                 
                             
                 
                 
                 
                 
                 
                 
                 
            else:
                
                print('Wrong shape!')
        
        
    elif choose=='2':
        
                
        
        
        
        
        
        while True:
            choose=input('choose the shape that you want(O/X):')
            
            
            
            
            
            if choose.upper()=='O':
                 name1=input('Enter human1 name:')
                
                 name2=input('Enter human2 name:')
                 name1=name1.lower()
                 name2=name2.lower()
                 opponents.append(f'{name1} VS {name2}')    
                 print(f'{name1} shape:O')
                 print(f'{name2} shape:X')
                 while True:
                     t1.show_table()
                     

                     print(f'{name1} turn')              
                     t1.choose=input('Choose the place:')
                     if t1.choose in t1.choices:
                         t1.put_up(t1.choose,'O')

                     else:
                         print('Try again!')
                         continue
                    
                     t1.conclusion()
                     if t1.conclusion()=='OOO':
                         t1.show_table()
                         print(f'{name1} won!')
                         winners.append(name1)
                         losers.append(name2)
                         break
                     elif t1.conclusion()=='XXX':
                         t1.show_table()
                         print(f'{name2} won!')
                         winners.append(name2)
                         losers.append(name1)
                         break
                     elif t1.conclusion()=='Tie':
                         t1.show_table()
                         print('Tie')
                         draws.append(f'{name1}={name2}')
                         break
                            

           
                         

                       
                     while True:
                         t1.show_table()
                         print(f'{name2} turn')
                         t1.choose=input('Choose the place:')
                         if t1.choose in t1.choices:
                             t1.put_up(t1.choose,'X')
                             break
                         else:
                             print('Try again!')


                    
                     t1.conclusion()
                     if t1.conclusion()=='OOO':
                         t1.show_table()
                         print(f'{name1} won!')
                         winners.append(name1)
                         losers.append(name2)
                         break
                     elif t1.conclusion()=='XXX':
                         t1.show_table()
                         print(f'{name2} won!')
                         winners.append(name2)
                         losers.append(name1)
                         break
                     elif t1.conclusion()=='Tie':
                         t1.show_table()
                         print('Tie')
                         draws.append(f'{name1}={name2}')
                         break
                                                        


                             

                         
                 break                          
                     
                     
                     
            elif choose.upper()=='X':
                 name1=input('Enter human1 name:')
                 name2=input('Enter human2 name:')
                 name1=name1.lower()
                 name2=name2.lower()                 
                 opponents.append(f'{name1} VS {name2}')               
                
                 print(f'{name1} shape:X')
                 print(f'{name2} shape:O')                  
                 
                 while True:
                     t1.show_table()
                     

                     print(f'{name1} turn')              
                     t1.choose=input('Choose the place:')
                     if t1.choose in t1.choices:
                         t1.put_up(t1.choose,'X')
                     else:
                         print('Try again!')
                         continue

                     t1.conclusion()
                     if t1.conclusion()=='OOO':
                         t1.show_table()
                         print(f'{name2} won!')
                         winners.append(name2)
                         losers.append(name1)
                         break
                     elif t1.conclusion()=='XXX':
                         t1.show_table()
                         print(f'{name1} won!')
                         winners.append(name1)
                         losers.append(name2)
                         break
                     elif t1.conclusion()=='Tie':
                         t1.show_table()
                         print('Tie')
                         draws.append(f'{name1}={name2}')
                         break
                                                 

                     while True:
                         t1.show_table()
                
                         print(f'{name2} turn')
                         t1.choose=input('Choose the place:')
                         if t1.choose in t1.choices:
                             t1.put_up(t1.choose,'O')
                             break
                         else:
                             print('Try again!')
                             


                     t1.conclusion()
                     if t1.conclusion()=='OOO':
                         t1.show_table()
                         print(f'{name2} won!')
                         winners.append(name2)
                         losers.append(name1)
                         break
                     elif t1.conclusion()=='XXX':
                         t1.show_table()
                         print(f'{name1} won!')
                         winners.append(name1)
                         losers.append(name2)
                         break
                     elif t1.conclusion()=='Tie':
                         t1.show_table()
                         print('Tie')
                         draws.append(f'{name1}={name2}')
                         break
                                                 

                             
                 break            
   
            else:
                print('Wrong shape!')
   
   
   
   
   
   
   
   
   
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    elif choose=='3':
        print('Players take turns putting their marks in empty squares. The first player to get 3 of her marks in a row (up, down, across, or diagonally) is the winner. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie')
    elif choose=='4':
        print(f'Human wins={human_wins}')

        print(f'Cpu wins={cpu_wins}')

        print(f'Draws={draw}')
    elif choose=='5':
        print(f'Opponents={opponents}')
        print(f'winners={winners}')
        print(f'losers={losers}')
        print(f'Draws={draws}')
        index=0
        for i in winners:
            print(f'{winners[index]} defeated {losers[index]}')
            
            index+=1
            
        dup=[]    
        for i in winners:
            if i not in dup:
                
                print(f'{i} wins={winners.count(i)}')
                dup.append(i)
        dup=[]
        for i in losers:
            if i not in dup:
                print(f'{i} loses={losers.count(i)}')
                dup.append(i)
                
    elif choose=='6':
        print('Exiting....') 
        open=False   
    else:
        print('Wrong command!')    
