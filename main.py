##Start
import math
balance=0
pin='0000'
deposit=recharge=0
send_money=pay_bill=0
##HOME Section
while True:
    print('\n---------*****-----------')
    print('  PYTHON CASH LIMITED')
    print('--------*****------------')
    print('\n[1] Check Balance\n[2] Add Money\n[3] Mobile Recharge\n[4] Send Money\n[5] Pay Bill\n[6] History\n[0] Exit')
    home = input('\nChoose Menu: ')
    
## Home [1] Start
    if home == '1':
        check_bl = input('Do you want to check Balance [y/n]: ')
        if check_bl == 'y' or check_bl == 'Y':
            
            in_pin=input('\nEnter Pincode: ')
            if in_pin == pin:
                print('\n** Check Balance **')
                print('\n------------------------')
                print(f'Current Balance: {balance}tk')
                print('------------------------')
                return_hm=input('\nReturn Home [H] / Exit [E]: ')
                if return_hm == 'H' or return_hm == 'h':
                    print('\n')
                elif return_hm == 'e' or return_hm == 'E':
                    print('\nEXIT !!\n')
                    break
                else:
                    print('\nReturn Home')
            else:
                print('\nPincode Not Match !!')
                in_pin=input('\nEnter Pincode Again: ')
                if in_pin == pin:
                    print('\n** Check Balance **')
                    print('\n------------------------')
                    print(f'Current Balance: {balance}tk')
                    print('------------------------')
                    return_hm=input('\nReturn Home [H] / Exit [E]: ')
                    if return_hm == 'H' or return_hm == 'h':
                        print('\n')
                    elif return_hm == 'e' or return_hm == 'E':
                        print('\nEXIT !!\n')
                        break
                else:
                    print('\nFailed, TRY AGAIN !!')   
        else:
            print('\nReturn Home')
## Home [1] End

## Home [2] strat
    elif home == '2':
        add_money_home = input('\nDo you want to Add Money [y/n]: ')
        if add_money_home == 'y' or add_money_home == 'Y':
            add_money=int(input('\nEnter Ammount: '))
            if add_money > 0:
                balance = balance + add_money
                deposit=deposit+add_money
                print(f"\n** {add_money}tk Add Money Sucessful **")
                return_hm=input('\nReturn Home [H] / Exit [E]: ')
                if return_hm == 'H' or return_hm == 'h':
                    print('\n')
                elif return_hm == 'e' or return_hm == 'E':
                    print('\nEXIT !!\n')
                    break
                else:
                    print('\nReturn Home')
            else:
                print('\nEnter Valid Ammount !')   
                
        else:
            print('\nReturn Home')
## Home [2] End

## Home [3] Start
    elif home == '3':
        mr_hm = input('\nDo you want to Mobile Recharge [y/n]: ')
        if mr_hm == 'y' or mr_hm == 'Y':
            in_pin=input('\nEnter Pincode: ')
            if in_pin == pin:
                mr_num = (input('\nEnter Number: +880-'))
                mr_ammount=int(input('Recharge Ammount: '))
                if mr_ammount >=20 and mr_ammount < balance:
                    number = len(mr_num)
                    if number == 11:
                        print(f"\n** {mr_ammount}tk, Recharge Sucessful at this number (+880-{mr_num}) **")
                        balance=balance-mr_ammount
                        recharge=recharge+mr_ammount
                        return_hm=input('\nReturn Home [H] / Exit [E]: ')
                        if return_hm == 'H' or return_hm == 'h':
                            print('\n')
                        elif return_hm == 'e' or return_hm == 'E':
                            print('\nEXIT !!\n')
                            break           
                else:
                    print('\nMobile Recharge Unsucessful !!')
                    return_hm=input('\nReturn Home [H] / Exit [E]: ')
                    if return_hm == 'H' or return_hm == 'h':
                        print('\n')
                    elif return_hm == 'e' or return_hm == 'E':
                        print('\nEXIT !!\n')
                        break
            else:
                print('\nPincode Not Match !!')
                in_pin=input('\nEnter Pincode Again: ')
                if in_pin == pin:
                    mr_num = (input('\nEnter Number: +880-'))
                    mr_ammount=int(input('Recharge Ammount: '))
                    if mr_ammount >=20 and mr_ammount < balance:
                        number = len(mr_num)
                        if number == 11:
                            print(f"\n** {mr_ammount}tk, Recharge Sucessful at this number (+880{mr_num}) **")
                            balance=balance-mr_ammount
                            recharge=recharge+mr_ammount
                            return_hm=input('\nReturn Home [H] / Exit [E]: ')
                            if return_hm == 'H' or return_hm == 'h':
                                print('\n')
                            elif return_hm == 'e' or return_hm == 'E':
                                print('\nEXIT !!\n')
                                break
                        else:
                            print('\nCheck Number !!')    
                    else:
                        print('\nMobile Recharge Unsucessful !!')
                        return_hm=input('\nReturn Home [H] / Exit [E]: ')
                        if return_hm == 'H' or return_hm == 'h':
                            print('\n')
                        elif return_hm == 'e' or return_hm == 'E':
                            print('\nEXIT !!\n')
                            break
                else:
                    print('\nFailed, TRY AGAIN !')
        else:
            print('\nReturn Home')                    
## Home [3] End

## Home [4] Start
    elif home == '4':
        sm_home = input('\nDo you want Send Money [y/n]: ')
        if sm_home == 'Y' or sm_home == 'y':
            in_pin=input('\nEnter Pincode: ')
            if in_pin == pin:
                print('\n** Send Money **')
                sm_num = (input('\nNumber : +880-'))
                number=len(sm_num)
                sm_ammount = int(input('Ammount: '))
                if (sm_ammount <= balance) and (number == 11):
                        balance= balance - sm_ammount
                        send_money=send_money+sm_ammount
                        print(f'\n**Send Money Successful**\n{sm_ammount}tk Send Money at this (+880-{sm_num}) number\nRemaning Balance: {balance}tk')
                        return_hm=input('\nReturn Home [H] / Exit [E]: ')
                        if return_hm == 'H' or return_hm == 'h':
                            print('\n')
                        elif return_hm == 'e' or return_hm == 'E':
                            print('\nEXIT !!\n')
                            break
                else:
                    print('\nSend Money Unsucessful !!')
            else:
                print('\nPincode Not Match !!')
                in_pin=input('\nEnter Pincode Again: ')
                if in_pin == pin:
                    print('\n** Send Money **')
                    sm_num = input('\nNumber : +880-')
                    number=len(sm_num)
                    sm_ammount = int(input('Ammount: '))
                    if (sm_ammount <= balance) and (number == 11):
                        balance = balance - sm_ammount
                        send_money=send_money+sm_ammount
                        print(f'\n**Send Money Successful**\n{sm_ammount}tk Send Money at this (+880-{sm_num}) number\nRemaning Balance: {balance}tk')
                        return_hm=input('\nReturn Home [H] / Exit [E]: ')
                        if return_hm == 'H' or return_hm == 'h':
                            print('\n')
                        elif return_hm == 'e' or return_hm == 'E':
                            print('\nEXIT !!\n')
                            break
                    else:
                        print('\nSend Money Unsucessfull !!')
                else:
                    print('\nPincode Not Match, TRY AGAIN !')
        else:
            print('\nReturn Home')
## Home [4] End

## Home [5] Start
    elif home == '5':
        pay_home = input('\nDo you want to Pay Bill [y/n]: ')
        if pay_home == 'y' or pay_home == 'Y':
            in_pin=input('\nEnter Pincode: ')
            if in_pin == pin:
                print('\n** Pay Bill **')
                print('\n[E] Electricity Bill\n[W] Water Bill\n[G] Gas Bill [H] Home')
                pay_choice=input('\nPay Bill Option: ')
                if pay_choice =='e' or pay_choice =='E':
                    pay_eb =input('Do you want to Pay Electricity Bill [y/n]: ')
                    if pay_eb =='Y'or pay_eb=='y':
                        print('\n** Pay Electricity Bill **')
                        pay_cn=input('\nEnter Bill Card Number: ')
                        pay_ammount=int(input('Pay Ammount: '))
                        if (pay_ammount <= balance) and (pay_ammount > 0):
                            balance = balance - pay_ammount
                            pay_bill=pay_bill+pay_ammount
                            print(f"\n**Electricity Bill Paid Sucessful**\nBill id: {pay_cn}\nTotal Pay: {pay_ammount}")
                            print(f'\nRemeanig Balance: {balance}tk')
                            return_hm=input('\nReturn Home [H] / Exit [E]: ')
                            if return_hm == 'H' or return_hm == 'h':
                                print('\n')
                            elif return_hm == 'e' or return_hm == 'E':
                                print('\nEXIT !!\n')
                                break
                        else:
                            print('\nElectricity Bill Payed Uncessfull !!')
                    else:
                        print('\nReturn Back') 
                           
                elif pay_choice == 'W'or pay_choice == 'w':
                    pay_eb =input('Do you want to Pay Water Bill [y/n]: ')
                    if pay_eb =='Y'or pay_eb=='y':
                        print('\n** Pay Water Bill **')
                        pay_cn=input('\nEnter Bill Card Number: ')
                        pay_ammount=int(input('Pay Ammount: '))
                        if (pay_ammount <= balance) and (pay_ammount > 0):
                            balance = balance - pay_ammount
                            pay_bill=pay_bill+pay_ammount
                            print(f"\n**Water Bill Paid Sucessful**\nBill id: {pay_cn}\nTotal Pay: {pay_ammount}")
                            print(f'\nRemeanig Balance: {balance}tk')
                            return_hm=input('\nReturn Home [H] / Exit [E]: ')
                            if return_hm == 'H' or return_hm == 'h':
                               print('\n')
                            elif return_hm == 'e' or return_hm == 'E':
                               print('\nEXIT !!\n')
                               break
                            else:
                                print('\nHome')
                        else:
                            print('\nWater Bill Payed Uncessfull !!')
                    else:
                        print('\nReturn Back')
                
                elif pay_choice == 'G' or pay_choice =='g':
                    pay_eb =input('Do you want to Pay Gas Bill [y/n]: ')
                    if pay_eb =='Y'or pay_eb=='y':
                        print('\n** Pay Gas Bill **')
                        pay_cn=input('\nEnter Bill Card Number: ')
                        pay_ammount=int(input('Pay Ammount: '))
                        if (pay_ammount <= balance) and (pay_ammount > 0):
                            balance = balance - pay_ammount
                            pay_bill=pay_bill+pay_ammount
                            print(f"\n**Gas Bill Paid Sucessful**\nBill id: {pay_cn}\nTotal Pay: {pay_ammount}")
                            print(f'\nRemeanig Balance: {balance}tk')
                            return_hm=input('\nReturn Home [H] / Exit [E]: ')
                            if return_hm == 'H' or return_hm == 'h':
                               print('\n')
                            elif return_hm == 'e' or return_hm == 'E':
                               print('\nEXIT !!\n')
                               break
                           
                        else:
                            print('\nGas Bill Payed Uncessfull !!')    
                else: 
                    print('\nRetun Home')
            else:
                print('\n!! Wrong Pincode !!')
                in_pin=input('\nEnter Pincode Again: ')
                if in_pin == pin:
                    print('\n** Pay Bill **')
                    print('\n[E] Electricity Bill\n[W] Water Bill\n[G] Gas Bill [H] Home')
                    pay_choice=input('\nPay Bill Option: ')
                    if pay_choice =='e' or pay_choice =='E':
                        pay_eb =input('Do you want to Pay Electricity Bill [y/n]: ')
                        if pay_eb =='Y'or pay_eb=='y':
                            print('\n** Pay Electricity Bill **')
                            pay_cn=input('\nEnter Bill Card Number: ')
                            pay_ammount=int(input('Pay Ammount: '))
                            if (pay_ammount <= balance) and (pay_ammount > 0):
                                balance = balance - pay_ammount
                                pay_bill=pay_bill+pay_ammount
                                print(f"\n**Electricity Bill Paid Sucessful**\nBill id: {pay_cn}\nTotal Pay: {pay_ammount}")
                                print(f'\nRemeanig Balance: {balance}tk')
                                return_hm=input('\nReturn Home [H] / Exit [E]: ')
                                if return_hm == 'H' or return_hm == 'h':
                                    print('\n')
                                elif return_hm == 'e' or return_hm == 'E':
                                    print('\nEXIT !!\n')
                                    break
                            else:
                                print('\nElectricity Bill Payed Uncessfull !!')
                        else:
                            print('\nReturn Back') 
                            
                    elif pay_choice == 'W'or pay_choice == 'w':
                        pay_eb =input('Do you want to Pay Water Bill [y/n]: ')
                        if pay_eb =='Y'or pay_eb=='y':
                            print('\n** Pay Water Bill **')
                            pay_cn=input('\nEnter Bill Card Number: ')
                            pay_ammount=int(input('Pay Ammount: '))
                            if (pay_ammount <= balance) and (pay_ammount > 0):
                                balance = balance - pay_ammount
                                pay_bill=pay_bill+pay_ammount
                                print(f"\n**Water Bill Paid Sucessful**\nBill id: {pay_cn}\nTotal Pay: {pay_ammount}")
                                print(f'\nRemeanig Balance: {balance}tk')
                                return_hm=input('\nReturn Home [H] / Exit [E]: ')
                                if return_hm == 'H' or return_hm == 'h':
                                    print('\n')
                                elif return_hm == 'e' or return_hm == 'E':
                                    print('\nEXIT !!\n')
                                    break
                            else:
                                print('\nWater Bill Pay Unsucessful !')
                        else:
                            print('\nReturn Home')
                    elif pay_choice == 'G' or pay_choice =='g':
                        pay_eb =input('Do you want to Pay Gas Bill [y/n]: ')
                        if pay_eb =='Y'or pay_eb=='y':
                            print('\n** Pay Gas Bill **')
                            pay_cn=input('\nEnter Bill Card Number: ')
                            pay_ammount=int(input('Pay Ammount: '))
                            if (pay_ammount <= balance) and (pay_ammount > 0):
                                balance = balance - pay_ammount
                                pay_bill=pay_bill+pay_ammount
                                print(f"\n**Gaas Bill Paid Sucessful**\nBill id: {pay_cn}\nTotal Pay: {pay_ammount}")
                                print(f'\nRemeanig Balance: {balance}tk')
                                return_hm=input('\nReturn Home [H] / Exit [E]: ')
                                if return_hm == 'H' or return_hm == 'h':
                                   print('\n')
                                elif return_hm == 'e' or return_hm == 'E':
                                   print('\nEXIT !!\n')
                                   break
                else:
                    print('\nWrong Pincode, TRY AGAIN !!')
## Home [5] End

## Home [6] Start
    elif home == '6':
        his_home = input('\nDo you to View History [y/n]: ')
        if his_home == 'Y' or his_home == 'y':
            in_pin=input('\nEnter Pincode: ')
            if in_pin == pin:
                print('\n** History **')
                if deposit > 0:
                    print(f'\nLast Deposit: {deposit}tk')
                if recharge > 0:
                    print(f'Total Recharge: {recharge}tk')
                if send_money > 0:
                    print(f'Total Send Money: {send_money}tk')
                if pay_bill > 0:
                    print(f'Total Pay Bill: {pay_bill}tk')
                return_hm=input('\nReturn Home [H] / Exit [E]: ')
                if return_hm == 'H' or return_hm == 'h':
                    print('\n')
                elif return_hm == 'e' or return_hm == 'E':
                    print('\nEXIT !!\n')
                    break
            else:
                print('\nWrong Pincode !!')
        else:
            print('\nReturn Home')
## Home [6] End

## Home [0] Exit Stat
    elif home == '0':
        exit_input=input('\nDo you want to Exit [y/n]: ')
        if exit_input == 'y' or exit_input == 'Y':
            print('\n**EXIT SUCESSFUL**\n--* Thank You *--\n')
            break
        else:
            print('\nReturn Home')
## Home [0] End


