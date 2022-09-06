# 用everything软件搜索 ".s7p" ,将所有文件的路径复制到字符串s中，本脚本可自动将step7程序的文件夹压缩，并将源文件夹删除
# 可以搜索“.mcp” ,可压缩wincc项目文件文件夹

import zipfile
import os
import re
import shutil

s = r"""D:\Work\Work_VC\Project_old\J金口\电气调试\s7_Eplan\UV.edb
D:\Work\Work_VC\Project_2021\2021年06月01日 200吨集装箱设备标准化\200T标准集装箱电气原理图3.1.edb
D:\Work\Work_VC\Project_2022\2022年01月21日 上饶返回200吨设备维修\200T标准集装箱电气原理图4.1.edb
D:\Work\Work_VC\Project_2022\2022年03月15日 潮南二期\潮南二期项目300T单级.edb
D:\Work\Work_VC\Project_2022\2022年04月01日 上饶返修300吨两套\300T两级DTRO就地箱.edb
D:\Work\Work_VC\Project_2022\2022年04月01日 上饶返修300吨两套\300T两级DTRO.edb
D:\Work\Work_VC\Project_2022\2022年06月16日 温州西向二期\电气设计\温州二期PLC柜原理图.edb（400PLC）\温州二期PLC柜原理图.edb
D:\Work\Work_VC\Project_2022\2022年06月16日 温州西向二期\电气设计\PLC柜原理图（独立412CPU版）\温州二期PLC柜原理图412.edb
D:\Work\Work_VC\Project_2022\2022年06月16日 温州西向二期\一期资料\温州项目_V7.2_20190327093519.edb
D:\Work\Work_VC\Project_2022\2022年06月16日 温州西向二期\电气设计\温州二期PLC柜原理图(1200).edb
D:\Work\Work++\其他人员项目移交备份\祖\19.04.19_2019备用（瑞能天地）200吨90Bar集装箱式两级DTRO2号\电气\2019备用（瑞能天地）200吨90Bar集装箱式两级DTRO2号\2019备用200吨90Bar集装箱DTRO2号.edb
D:\Work\Work_VC\Project_2022\2022年06月16日 温州西向二期\电气设计\温州二期PLC柜原理图.edb（400PLC）
D:\Work\Work_VC\Project_2022\2022年01月11日 北京南宫\南宫项目电气原理图.edb
D:\Work\Work_VC\Project_2022\2022年04月24日 银川零排放项目\电气设计\固化系统\银川项目固化系统.edb
D:\Work\Work_VC\Project_2022\2022年03月09日 巢湖污泥项目\电气设计\Eplan电气原理图\预处理PLC柜01柜.edb
D:\Work\Work_VC\Project_old\W温州西向\设计中……\备份\Eplan温州2016年6月28日\温州项目.edb
D:\Work\Work_VC\Project_2022\2022年04月24日 银川零排放项目\电气设计\银川项目电控柜.edb
D:\Work\Work_VC\Project_old\W温州西向\设计中……\备份\Eplan温州2016年6月28日\温州项目_V7.2_20220620090548\温州项目.edb
D:\Work\Work_VC\Project_2022\2022年06月07日 新实验室配电箱\实验室动力配电箱.edb
D:\Work\Work_VC\Project_2022\2022年03月02日 上饶新增345集装箱\200T标准集装箱电气原理图5.1.edb
D:\Work\Work++\其他人员项目移交备份\张宇航移交\长山口项目\600t\电气\电气图纸\长山口新增租赁标准200t3号两级DTRO.edb
D:\Work\Work++\其他人员项目移交备份\张宇航移交\长山口项目\600t\电气\电气图纸\长山口新增租赁标准200t2号两级DTRO.edb
D:\Work\Work_VC\Project_2022\2022年03月09日 巢湖污泥项目\电气设计\Eplan电气原理图\预处理PLC柜02柜.edb
D:\Work\Work++\其他人员项目移交备份\陈奕然资料\42 广州危废项目\图纸\广州危废图纸\广州危废项目DTRO膜系统B.edb
D:\Work\Work++\其他人员项目移交备份\陈奕然资料\42 广州危废项目\图纸\广州危废图纸\广州危废项目DTRO膜系统A.edb
D:\Work\Work++\其他人员项目移交备份\陈奕然资料\42 广州危废项目\图纸\广州危废图纸\广州危废项目DTRO罐系统.edb
D:\Work\Work++\其他人员项目移交备份\张鹏移交\0.1设计项目\2.0DTRO注杀菌剂保护液设备\DTRO注杀菌剂保护液设备.edb
D:\Work\Work++\其他人员项目移交备份\张鹏移交\0.1设计项目\1.0D低温蒸发项目\截图与新建项目\低温蒸发系统.edb
D:\Work\Work++\其他人员项目移交备份\张鹏移交\0.1设计项目\1.0D低温蒸发项目\图纸\低温蒸发中试设备.edb
D:\Work\Work++\其他人员项目移交备份\张鹏移交\0.1设计项目\1.0D低温蒸发项目\1.电控室备份文件\电气资料\低温蒸发中试设备.edb
D:\Work\Work++\其他人员项目移交备份\张鹏移交\0.1设计项目\0.1参考项目\DTRO图纸_最终\DTRO图纸_最终.edb
D:\Work\Work_VC\投标2020\南昌深度处理系统2020年12月1日\NF系统一次系统图.edb
D:\Work\Work_VC\Project_2022\2022年04月01日 上饶返修300吨两套\江西南城300T两级DTRO\江西南城300T两级DTRO\300T两级DTRO.edb
D:\Work\Work_VC\Project_2021\2021年03月12日 张浩2\新项目.edb
D:\Work\Work_VC\Project_2021\2021年03月02日 张浩1\AP3_PLC柜原理图.edb
D:\Work\Work++\其他人员项目移交备份\刘海燕\2019年项目\5月TDR-011210098渭南项目100T\电气设计\渭南项目.edb
D:\Work\Work++\其他人员项目移交备份\刘海燕\2018年项目\沈阳大辛\大辛就地箱原理图.edb
D:\Work\Work++\其他人员项目移交备份\刘海燕\2018年项目\3月常山\新项目.edb
D:\Work\Work++\其他人员项目移交备份\刘海燕\2018年项目\3月常山\常山项目.edb
D:\Work\Work_VC\Project_2022\2022年03月09日 巢湖污泥项目\电气设计\罐系统（祖洪玉负责）\巢湖罐系统.edb
D:\Work\Work_VC\Project_2022\2022年04月06日 张浩\ACS01+1.edb
D:\Work\Work_VC\Project_2022\2022年02月28日 达旗碳化硅改造\达旗项目碳化硅改造.edb
D:\Work\Work_VC\Project_2019\100吨集装箱项目1500PLC\电气原理图(100T).edb
D:\Work\Work++\其他人员项目移交备份\张宇航移交\长山口项目\600t\电气\电气图纸\长山口新增租赁标准200t罐系统.edb
D:\Work\Work++\其他人员项目移交备份\张宇航移交\长山口项目\600t\电气\电气图纸\长山口新增租赁标准200t1号两级DTRO.edb
D:\Work\Work++\其他人员项目移交备份\张鹏移交\0.1设计项目\0.1参考项目\碳化硅小试20200509\碳化硅小试20200509\碳化硅小试20200509.edb
D:\Work\Work_VC\Project_2022\2022年01月21日 上饶返回200吨设备维修\长山口第一套\长山口新增租赁标准200t1号两级DTRO.edb
D:\Work\Work_VC\Project_2021\2021年12月23日 北京南宫项目\160BarDTRO中试设备.edb
D:\Work\Work_VC\Project_2019\160Bar中试设备自动化改造2019年2月18日\160BarDTRO中试设备.edb
D:\Work\Work_VC\project_2020\黄骅（中节能）\电气设计\70吨单级DTRO电气原理图.edb
D:\Work\Work_VC\project_2020\将乐50t\电气设计\标准两级DT（将乐）.edb
D:\Work\Work_VC\project_2020\越南北宁\电气设计\100T标准单级DTRO.edb
D:\Work\Work_VC\Project_2021\2021年03月02日 张浩1\AP4_PLC柜原理图.edb
D:\Work\Work_VC\project_2020\H黄陵30T\电气设计\30T标准两级DT.edb
D:\Work\Work_VC\project_2020\标准100T两套2020年5月22日\1#电气设计\100T标准两级DT.edb
D:\Work\Work_VC\Project_old\B碧水源\软启动器控制箱.edb
D:\Work\Work++\其他人员项目移交备份\刘海燕\2019年项目\11月海螺酒泉\海螺酒泉项目资料-发电气\海螺酒泉项目资料-发电气\电气设计\酒泉项目125T电气原理图.edb
D:\Work\Work++\其他人员项目移交备份\刘海燕\2021年项目\广州危废\电气\膜系统\膜系统A\广州危废项目DTRO膜系统A.edb
D:\Work\Work++\其他人员项目移交备份\刘海燕\2021年项目\广州危废\电气\罐系统电气\广州危废项目DTRO罐系统.edb
D:\Work\Work++\其他人员项目移交备份\刘海燕\2021年项目\广州危废\电气\膜系统\膜系统B\广州危废项目DTRO膜系统B.edb
D:\Work\Work_VC\project_2020\东光项目\电气\东光项目软化系统.edb
D:\Work\Work_VC\Project_2021\2021年03月24日 150吨设备\150T标准两级DT.edb
D:\Work\Work_VC\project_2020\DT设备标准化文件\所有吨位电气设计汇总\200T标准两级DT.edb
D:\Work\Work_VC\project_2020\DT设备标准化文件\所有吨位电气设计汇总\150T标准两级DT.edb
D:\Work\Work++\其他人员项目移交备份\刘海燕\2019年项目\11月海螺酒泉\海螺酒泉项目资料-发电气\海螺酒泉项目资料-发电气\电气设计\酒泉项目150T电气原理图.edb
D:\Work\Work_VC\project_2020\潍坊\电气原理图.edb
D:\Work\Work++\其他人员项目移交备份\刘海燕\2019年项目\10月沧州项目\沧州项目电气原理图.edb
D:\Work\Work++\其他人员项目移交备份\刘海燕\2019年项目\10月沧州项目\海螺霍山项目100T电气原理图.edb
D:\Work\Work++\其他人员项目移交备份\刘海燕\2019年项目\10月沧州项目\沧州电气\罐系统\沧州项目300T罐系统电气原理图.edb
D:\Work\Work++\其他人员项目移交备份\刘海燕\2018年项目\10月川宁改造\川宁参考\川宁参考\DTL-RO(共8套).edb
D:\Work\Work++\其他人员项目移交备份\刘海燕\2019年项目\10月中节能临沂\膜系统\临沂项目1000T电气原理图.edb
D:\Work\Work++\其他人员项目移交备份\刘海燕\2019年项目\10月中节能临沂\罐系统\沧州项目300T罐系统电气原理图.edb
D:\Work\Work++\其他人员项目移交备份\刘海燕\2019年项目\10月中节能临沂\罐系统\临沂项目1000T罐系统电气原理图.edb
D:\Work\Work++\其他人员项目移交备份\刘海燕\2021年项目\其他\FIP仪表项目\新建文件夹\新建文件夹\中节能汉中60t90bar单级DT.edb
D:\Work\Work++\其他人员项目移交备份\刘海燕\2020年项目\海螺危废300T\撬装电气设计DTLRO\锦州危废项目DTLRO.edb
D:\Work\Work++\其他人员项目移交备份\刘海燕\2020年项目\海螺危废300T\撬装电气设计HPRO\锦州危废项目HPRO.edb
D:\Work\Work_VC\project_2020\越南北宁\电气设计\祖洪玉\发陈工20201204\uf\越南北宁UF.edb
D:\Work\Work_VC\project_2020\越南北宁\电气设计\祖洪玉\发陈工20201204\100T标准单级DTRO\100T标准单级DTRO.edb
D:\Work\Work_VC\project_2020\DT设备标准化文件\所有吨位电气设计汇总\10T标准两级DT.edb
D:\Work\Work_VC\project_2020\东光项目\电气\200T单级DT.edb
D:\Work\Work_VC\project_2020\略阳60吨两级DTRO+离子交换2020年5月25日\60吨项目两级DTRO.edb
D:\Work\Work++\其他人员项目移交备份\刘海燕\2018年项目\沈阳老虎冲\沈阳老虎冲20180110\沈阳老虎冲\参考资料\老虎冲\一次系统图.edb
D:\Work\Work++\其他人员项目移交备份\刘海燕\2018年项目\8月榆林\榆林.edb
D:\Work\Work_VC\project_2020\山西文水50T\电气设计\50T标准两级DT.edb
D:\Work\Work_VC\project_2020\长山口1000吨移机\长山口1000吨移机罐系统.edb
D:\Work\Work_VC\Project_2021\2021年03月10日 张北项目\Z张北项目\电气\撬装设备\DT设备\海螺张北_175吨单级DTRO电气原理图.edb
D:\Work\Work_VC\Project_2019\利川30\DTRO图纸_最终\湖北利川项目30吨.edb
D:\Work\Work++\其他人员项目移交备份\刘海燕\2020年项目\校对\北宁给刘工\北宁给刘工\电气\uf\越南北宁UF.edb
D:\Work\Work++\其他人员项目移交备份\刘海燕\2020年项目\校对\北宁给刘工\北宁给刘工\电气\100T标准单级DTRO\100T标准单级DTRO.edb
D:\Work\Work++\其他人员项目移交备份\刘海燕\2019年项目\9月满洲里\满洲里电气\满洲里项目100T电气原理图.edb
D:\Work\Work++\其他人员项目移交备份\刘海燕\2019年项目\6月赣州\赣州二期项目电气原理图.edb
D:\Work\Work++\其他人员项目移交备份\刘海燕\2019年项目\5月霍山\电气\海螺霍山项目100T电气原理图.edb
D:\Work\Work++\其他人员项目移交备份\刘海燕\2019年项目\5月霍山\电气\榆林项目DTRO电气原理图.edb
D:\Work\Work++\其他人员项目移交备份\刘海燕\2019年项目\5月景洪改造\电气标准图纸.edb
D:\Work\Work++\其他人员项目移交备份\刘海燕\2019年项目\5月景洪改造\景洪改造项目电气原理图.edb
D:\Work\Work++\其他人员项目移交备份\刘海燕\2019年项目\5月景洪改造\2018备用150TD两级DTRO（75BAR)1号-1129\2018备用150TD两级DTRO（75BAR)1号-1129.edb
D:\Work\Work++\其他人员项目移交备份\刘海燕\2019年项目\5月TDR-011210098渭南项目100T\渭南项目DTRO电气原理图.edb
D:\Work\Work++\其他人员项目移交备份\刘海燕\2019年项目\5月TDR-011210098渭南项目100T\渭南项目DRO电气原理图.edb
D:\Work\Work++\其他人员项目移交备份\刘海燕\2019年项目\5月TDR-011210098渭南项目100T\抚州项目电气原理图.edb
D:\Work\Work++\其他人员项目移交备份\刘海燕\2019年项目\2月抚州\电气设计\抚州电气原理图20190315\抚州项目电气原理图.edb
D:\Work\Work++\其他人员项目移交备份\刘海燕\2019年项目\3月海螺石柱\海螺石柱项目电气原理图.edb
D:\Work\Work++\其他人员项目移交备份\刘海燕\2019年项目\2月衡阳项目\衡阳项目新增NF电气原理图.edb
D:\Work\Work++\其他人员项目移交备份\刘海燕\2019年项目\2月抚州\电气设计\电气增加预处理\抚州项目电气原理图.edb
D:\Work\Work++\其他人员项目移交备份\刘海燕\2019年项目\2月抚州\电气设计\抚州项目预处理电气原理图.edb
D:\Work\Work++\其他人员项目移交备份\刘海燕\2019年项目\12月锦信禹州\电气\赣州二期项目电气原理图.edb
D:\Work\Work++\其他人员项目移交备份\刘海燕\2019年项目\2月抚州\EPLAN_电动机断路器版.edb
D:\Work\Work++\其他人员项目移交备份\杨交接\1plan\复制 金华一次图.edb
D:\Work\Work++\其他人员项目移交备份\杨交接\1plan\w温岭\温岭.edb
D:\Work\Work++\其他人员项目移交备份\杨交接\1plan\h汉中\汉中图纸.edb
D:\Work\Work++\其他人员项目移交备份\杨交接\1plan\d大理\大理.edb
D:\Work\Work++\其他人员项目移交备份\杨交接\0project\p浦江\电气-施工图\膜车间\浦江项目.edb
D:\Work\Work++\其他人员项目移交备份\杨交接\0project\p浦江\电气-施工图\膜车间\复制 浦江项目.edb
D:\Work\Work++\其他人员项目移交备份\杨交接\0project\n南昌\电气施工图\za\原理图.edb"""


s2 = s.split("\n")
print(s2)


base_name = r'C:\Users\vm\Desktop'


# shutil.make_archive("A", "zip", root_dir='C:\\Users\\vm\\Desktop\\新建文件夹')
# dir=r'C:\Users\vm\Desktop\WinCC_20190327'


def zipDir(dirpath, p):
    # """
    # 压缩指定文件夹
    # :param dirpath: 目标文件夹路径
    # :param outFullName: 压缩文件保存路径+xxxx.zip
    # :return: 无
    # """
    # print(out.)

    s = dirpath.rfind("\\")
    d1 = dirpath[0:s]
    d2 = "Eplan_" + dirpath[s + 1:] + "." + p
    print(d1 + "\\" + d2)

    zip = zipfile.ZipFile(d1 + "\\" + d2, "w", zipfile.ZIP_DEFLATED)
    d = dirpath.replace(".edb",".elk")
    d3 = dirpath.replace(d1,"")
    d4= d3.replace(".edb",".elk")

    zip.write(d,d4)


    for path, dirnames, filenames in os.walk(dirpath):
        # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
        # print(path)
        fpath = path.replace(d1, '')
        # print(fpath)
        for filename in filenames:
            zip.write(os.path.join(path, filename), os.path.join(fpath, filename))
            #print((d1+"\\"+filename))
            pass
    zip.close()


# zipDir(dir,"zip")
for i in range(len(s2)):
    print(s2[i])
    dirpath = str(s2[i])    
    d = dirpath.replace(".edb",".elk")
    print(d)
    try:
        zipDir(dirpath , "zip")   #压缩文件夹
        try:               #删除压缩有的文件夹
            shutil.rmtree(dirpath)
            os.remove(d)        
        except:
            print(d)
            # pass
    except:
        pass

