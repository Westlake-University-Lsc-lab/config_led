import pyvisa
import sys
pulse_generator = 'USB0::0xF4EC::0x1101::SDG6XFCD7R0976::INSTR'
def configure_waveform_generator(     
    fre: int = 50, 
    amp: float = 1.8,   
    delay: int = 5
    ):
    rm = pyvisa.ResourceManager()
    afg = rm.open_resource(pulse_generator)
    
    SYNC_CH = 'CH2'
    afg.write('C2:SYNC ON, TYPE,{}'.format(SYNC_CH))
    print(r'external trigger Sync with {}'.format(SYNC_CH))
    # if delay <= 5:
    #     print(r'external trigger Sync with S1, delay time:{}'.format(delay))
    #     SYNC_CH = 'CH1'
    #     afg.write('C1:SYNC ON, TYPE,{}'.format(SYNC_CH))
    # elif delay > 5:
    #     print(r'delay time {} us large than 5us, external trigger Sync with S2'.format(delay))
    #     SYNC_CH = 'CH2'
    # afg.write('C2:SYNC ON, TYPE,{}'.format(SYNC_CH))

    # print(r'SYNC_CH:{}'.format(SYNC_CH))
    # if amp != offset+offset:
    #     print(r'amp:{} != 2*offset:{}'.format(amp,2*offset))
    #     print('Warning: Amplitude and offset are not correctly, please check!')
    #     sys.exit()
        
    afg.write('C1:CoMBiNe ON')

    # 配置输出通道的命令
    commands = [  
        'C1:OUTP ON',
        'C1:OUTP LOAD,50',
        'C1:OUTP PLRT,NOR',
        'C1:BSWV WVTP,PULSE',  
        'C2:OUTP ON',
        'C2:OUTP LOAD,50',
        'C2:OUTP PLRT,NOR',
        'C2:BSWV WVTP,PULSE', 
        'C1:BSWV FRQ,{}'.format(fre),      # 频率配置为50 Hz
        'C2:BSWV FRQ,{}'.format(fre),      # 频率配置为50 Hz
        'C2:BSWV AMP,1.36',                # 幅度配置为1.36 V
        'C2:BSWV OFST,680.E-3',            # 偏移量配置为780 mV
        r'C1:BSWV AMP,{}'.format(amp),     # 幅度配置为1.8V
        r'C1:BSWV OFST,{}'.format(amp/2.),  # 偏移量配置为900 mV (即0.9 V)
        'C1:BSWV WIDTH,150.E-9',  # S1脉冲宽度固定为150纳秒 (ns)
        'C2:BSWV WIDTH,1000.E-9',  # S2脉冲宽度固定为1us
        'C1:BSWV RISE, 1.E-9',   # 上升时间固定为1纳秒 (ns)
        'C1:BSWV FALL, 1.E-9', # 下降时间固定为1纳秒 (ns)
        'C2:BSWV RISE, 1.E-9',   # 上升时间固定为1纳秒 (ns)
        'C2:BSWV FALL, 1.E-9', # 下降时间固定为1纳秒 (ns)
        'C1:BSWV DLY, 0',      # CH1没有延迟, 单位为微秒 (us)
        'C2:BSWV DLY, {}.E-6'.format(delay),      # CH2延迟时间配置, 单位为微秒 (us)
    ]
    
    # 执行配置命令
    for command in commands:
        afg.write(command)       
    print('Finished configuring') 
    # 关闭资源（如果需要）
    afg.close()  # 如果不再需要保持连接可以注释掉或删除这行代码
    #return afg
    
def pulse_generator_configure():
    rm = pyvisa.ResourceManager()
    afg = rm.open_resource(pulse_generator)
    rm_address = rm.list_resources()
    config_info=[
        '*IDN?',
        'C1:SYNC?',
        'C2:SYNC?',
        'C1:CoMBiNe?',
        'C2:CoMBiNe?',
        'C1:OUTP?',
        'C2:OUTP?' ,       
    ]
    print(rm_address, type(rm_address))    
    for info in config_info:
        # print('----------\n')
        print(afg.query(info))
        # print(afg.query())
    afg.close()
