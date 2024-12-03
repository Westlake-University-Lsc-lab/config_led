import os
import sys

def check_type(input_param):
    #检查输入的参数是数字还是字符串
    if isinstance(input_param, str):
        # print("输入参数是字符串。")
        return False
    elif isinstance(input_param, (int, float)):
        # print("输入参数是数字。")
        return True
    else:
        print("Please input a valid parameter type.")

def find_parameter_key_index(line, para_map):
    for key in para_map:
        if line.startswith(key + ' '):  # 检查行首是否有符合键值+空格的开头部分
            # print("find key:{} with len:{}".format(key,len(key) + 1), type(len(key) + 1))            
            return len(key) + 1  # 如果找到匹配，则返回其位置（下标）的加一位置，用于之后的分割操作
    return None  

def find_str_no_empty(line):
    index = line.find(' ')
    if index != -1:  # 如果找到了空格
        return line[:index]
    else:
        return line

def check_match_in_map(para_map, str_to_check):
    if str_to_check in para_map:
        return True  
    else:
        return False  
    
    
def para_map_gen(trigger_style):
    if trigger_style == 'ext':
        para_map = {
            'OUTFILE_PATH': '/mnt/data/PMT/R8520_406/',
            'OUTFILE_NAME': 'lv2415_lv2414_20241126_12DB_LED_combine_1p7v_850mv_1p36v_680mv_5us_50hz_run0',
            'EXTERNAL_TRIGGER': 'ACQUISITION_ONLY',
            'SELF_TRIGGER': 'NO',
            'RECORD_LENGTH': '175'
        }
        if len(sys.argv) != 4:
            print("USAGE: python write_config.py trig_style rec_len file_name")
            return para_map
        elif len(sys.argv) == 4:
            if check_type(sys.argv[2]) == True:
                para_map['RECORD_LENGTH'] = sys.argv[2]
            if check_type(sys.argv[3]) == False:
                para_map['OUTFILE_NAME'] = sys.argv[3]
            return para_map
    elif trigger_style == 'self':
        para_map = {
            'OUTFILE_PATH': '/mnt/data/PMT/R8520_406/',
            'OUTFILE_NAME': 'lv2415_lv2414_20241118_darkrate_run0',
            'EXTERNAL_TRIGGER': 'DISABLE',
            'SELF_TRIGGER': 'YES',
            'RECORD_LENGTH': '40',
            'TRG_THRESHOLD': '20'
        }
        if len(sys.argv) != 5:
            print("USAGE: python write_config.py trig_style rec_len threshold file_name")
            return para_map
        elif len(sys.argv) == 5:
            if check_type(sys.argv[2]) == True:
                para_map['RECORD_LENGTH'] = sys.argv[2]
            if check_type(sys.argv[3]) == True:
                para_map['TRG_THRESHOLD'] = sys.argv[3]
            if check_type(sys.argv[4]) == False:
                para_map['OUTFILE_NAME'] = sys.argv[4]
        return para_map
    else:
        print("无效的触发器类型")
        return None

def replace_parameters_in_config(para_map, config_file):
    print("Writing new configuration file...")
    with open(config_file, 'r') as file:
        lines = file.readlines()
    new_lines = [] 
    for line in lines:
        # 跳过空行        
        if line.strip() == '':   
            continue  
        # 如果这一行是带 '#' 的注释行，则直接保留到新文件中
        if line.strip().startswith('#'):
            new_lines.append(line)  # 直接添加到新文件中的列表中
            continue  # 跳过进一步的参数替换检查，因为注释行不参与参数替换
        
        key_index = find_parameter_key_index(line, para_map)  # 查找行首至空格处是否存在键值并获取索引
        if key_index is not None:
            key, value = line.split(' ', 1)  
            new_line = f"{key} {para_map[key]}\n"
            new_lines.append(new_line)  # 将新生成的行加入到新文件中
            continue
        else:  # 如果没有找到匹配的键进行替换，则保留原始行（包含注释）
            new_lines.append(line)
      
    with open('configure_new.txt', 'w') as newfile: 
        for line in new_lines:
            newfile.write(line)  # 将每行内容写入新文件
        newfile.write('\n')   
        
    print("New configuration file has been written to 'configure_new.txt'.")
                                                    

def main():
    if len(sys.argv) < 2:
        print("Please input a valid trigger style.")
        print("USAGE: python write_config.py trig_style")
        sys.exit(1)
    config_file_path = '/home/yjj/pulse_gen/DAW_Config.txt'
    trigger_style = sys.argv[1]  
    para_map = para_map_gen(trigger_style)
    replace_parameters_in_config(para_map, config_file_path)

if __name__ == "__main__":
    main()