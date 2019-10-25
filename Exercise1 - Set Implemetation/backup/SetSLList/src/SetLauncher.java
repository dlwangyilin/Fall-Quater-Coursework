import java.io.*;

public class SetLauncher {
    public static void main(String[] args) {
        SetLL s1 = new SetLL();
        System.out.println("---------Part 1: Insert to the Set-----------------------");
        String pathname = "pride-and-prejudice.txt";
        try (FileReader reader = new FileReader(pathname);
             BufferedReader br = new BufferedReader(reader) // 建立一个对象，它把文件内容转成计算机能读懂的语言
        ) {
            String line;
            //网友推荐更加简洁的写法
            while ((line = br.readLine()) != null) {
                // 一次读入一行数据
                if(line.length()==0){
                    continue;
                }
                String[] str = line.split("\\s+");
                for(String sds :str){
                    sds = sds.replaceAll("\\pP","");
                    long startTime=System.nanoTime();
                    if(s1.add(sds)){
                        long endTime=System.nanoTime();
                        String num = String.valueOf(endTime-startTime);
                        writeFile("insert.txt", num);
                    }
                }

            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        System.out.println(s1.size());
        System.out.println("---------Part 2: How many words not included-------------");
        String pathname2 = "words-shuffled.txt";
        int notinclude = 0;
        try (FileReader reader = new FileReader(pathname2);
             BufferedReader br = new BufferedReader(reader) // 建立一个对象，它把文件内容转成计算机能读懂的语言
        ) {
            String line2;
            //网友推荐更加简洁的写法
            while ((line2 = br.readLine()) != null) {
                // 一次读入一行数据
                if(line2.length()==0){
                    continue;
                }
                String[] str = line2.split("\\s+");
                for(String sds :str){
                    sds = sds.replaceAll("\\pP","");
                    long startTime2=System.nanoTime();
                    if(!s1.contains(sds)){
                        notinclude ++;
                    }
                    long endTime2=System.nanoTime();
                    String num = String.valueOf(endTime2-startTime2);
                    writeFile("search.txt", num);
                }

            }
        } catch (IOException e) {
            e.printStackTrace();
        }
        System.out.println(notinclude);

    }
    private static void writeFile(String name, String num) {
        try {
            File writeName = new File(name); // 相对路径，如果没有则要建立一个新的output.txt文件
            writeName.createNewFile(); // 创建新文件,有同名的文件的话直接覆盖
            try (FileWriter writer = new FileWriter(writeName,true);
                 BufferedWriter out = new BufferedWriter(writer)
            ) {
                out.write(num); // \r\n即为换行
                out.write("\r\n");
                out.flush(); // 把缓存区内容压入文件
            }
        } catch (IOException e) {
            e.printStackTrace();
        }
    }

}
