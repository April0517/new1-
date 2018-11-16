def save_file(figure1,figure2,count):
    file_name_figure1='figure_'+str(count)+'.txt'
    file_name_figure2='figure_'+str(count)+'.txt'

    figure1=open(file_name_figure1,'w')
    figure2=open(file_name_figure2,'w')

    figure1.writelines(figure1)
    figure2.writelines(figure2)

    figure1.close()
    figure2.close()

def split_file(file_name):
    f=open(file_name)

    figure1=[]
    figure2=[]
    count=1

    for each_line in f:
        (role,line_spoken)=each_line.split(':',1)
        if role=='figure1':
            figure1.append(line_spoken)
        if role=='figure2':
            figure2.append(line_spoken)
        save_file(figure1,figure2,count)

        figure1=[]
        figure2=[]
        count=count+1

    save_file(figure1,figure2,count)
    f.close()

split_file('G:\\test.txt')
