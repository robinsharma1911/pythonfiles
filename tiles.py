
ini_state = {'t1':1,'t2':2,'t3':3,'t4':4,'t5':0,'t6':6,'t7':7,'t8':5,'t9':8}

final_state = {'t1':1,'t2':2,'t3':3,'t4':4,'t5':5,'t6':6,'t7':7,'t8':8,'t9':0}

mid_state = ini_state


def tiles(mid_state):

    if mid_state['t5'] == 0:

      
        mid_state['t5'] = mid_state['t8']
        mid_state['t8'] = 0
        tiles(mid_state)
    
    elif mid_state['t8'] == 0:
    
        mid_state['t8'] = mid_state['t9']
        mid_state['t9'] = 0
        tiles(mid_state)

    elif mid_state == ini_state:
        print(mid_state)
        return 1


tiles(mid_state)
