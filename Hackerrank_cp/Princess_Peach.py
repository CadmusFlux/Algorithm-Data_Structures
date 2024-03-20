    m_pos = None
    p_pos = None
    
    for idx,val in enumerate(grid):

        if 'p' in val:
            p_pos = [idx,val.index('p')]
        if 'm' in val:
            m_pos = [idx,val.index('m')]
            
    steps = []
        
    print(m_pos,p_pos)
    value0 = m_pos[0] - p_pos[0]
    value1 = m_pos[1] - p_pos[1]
    
    if value0>0: 
        steps.append(abs(value0)*'TOP')
    else:
        steps.append(abs(value0)*'DOWN')
        
    if value1>0: 
        steps.append(abs(value1)*'LEFT')
    else:
        steps.append(abs(value1)*'RIGHT')
    
    for i in range(len(steps)):
        
        print(steps[i])
