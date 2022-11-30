import os
import shutil
# import pdb

pngfiles = os.listdir("E:/gt_lungpng/")
pf = []
for pngfile in pngfiles:
    pf.append(pngfile.split('.')[0])
    print(pngfile.split('.')[0])
 
def wash_gt(old_path, new_path):
    
    # filename_list = os.listdir(old_path)
    # filearr = []
    
    filename_list = os.listdir(new_path)
    
    for i in filename_list:
        
        '''复制符合条件的raw至gt_lung'''
        
        # name = i.split('-')[0]
        # if name != "lung":
        #     continue
        # filename = i.split('_')[0]
        # dose = i.split('_')[1]
        
        # if filename not in filearr:
        #     filearr.append(filename)
        #     flag = False
        # if dose == 'dose20' and flag == False:
        #     # pdb.set_trace()
        #     # if i.split('_')[0] not in pf or i.split('_')[-1]=='10.raw':
        #     if i.split('_')[0] not in pf and i.split('_')[-1]=='1.raw':    
        #         # if i.split('_')[-1]=='10.raw':
        #         #     pf.append(i.split('_')[0])
        #         #     print(i)
        #         #     continue
        #         continue
            
        #     shutil.copy(os.path.join(old_path,i), new_path)
        #     flag = True
        #     print("{} is saved!".format(i))
            
            
        '''对照gt_png删数据'''
        filename = i.split('.')[0]
        if filename not in pf:
            os.remove(os.path.join(new_path,i))
            print(filename)
        
        


if __name__=='__main__':
    old_path = "E:/gt/"
    new_path = "E:/gt_lung/"
    if not os.path.isdir(new_path):
        os.mkdir(new_path)
    wash_gt(old_path, new_path)