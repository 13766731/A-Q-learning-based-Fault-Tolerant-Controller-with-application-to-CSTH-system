from utils import *


while loop_circle < 100:
    if loop_circle == 0:
            y_out[loop_circle] = CSTH_model(initial_inpute+fault_actuator)+fault
            error_mse[loop_circle] = np.sqrt((set_point - y_out[loop_circle])**2)
            error =   set_point - y_out[loop_circle]
            state = Enter_state(error)
    else:

        
        alpha=1#float(input('Enter alpha:   '))
        gama=1# float(input('Enter gama:   '))
        epsilon = 0
        # Q=np.random.rand(np.size(state11),np.size(actions11))
        # Q[0,:]=0
        # Q = np.zeros((np.size(state11),np.size(actions11)))
        A = Policy(Q,state,epsilon)
        S_perim,a = State(A,initial_inpute,fault,CSTH_model,fault_actuator)
        R = Reward(S_perim)
        Q[state,A+5] = Q[state,A+5] + alpha * (R + gama * max(Q[S_perim,:])-Q[state,A+5])
        state = S_perim
        y_out[loop_circle] = a
        error_mse[loop_circle] = np.sqrt((set_point - y_out[loop_circle])**2)
        # system_performance[loop_circle] = CSTH_model(initial_inpute)+fault

        # (A,y_out,loop_circle,loop_Q_Learning,error_mse) = Q_Learning_Algorithm (fault,state,State,Reward,Policy,CSTH_model,loop_circle,y_out,error_mse)
        
    loop_circle += 1
    fault += 0.01


###################################### PID controller ############


y_out_pid = np.zeros(300)
error_mse_pid= np.zeros(300)
loop_circle=0
error = 0
a=0
yy =0
ii =0
initial_inpute = 1
set_point = 15
fault = 4
while loop_circle <100:
    
                control_action = PID_controller(CSTH_model,y_out_pid[loop_circle])+ fault_actuator
                y_out_pid[loop_circle] = CSTH_model(control_action) + fault
                error_mse_pid[loop_circle] = np.sqrt((15 - y_out_pid[loop_circle])**2)
                fault += 0.01
                loop_circle += 1
                

                


print(sum(abs(error_mse)))
print(sum(abs(error_mse_pid)))