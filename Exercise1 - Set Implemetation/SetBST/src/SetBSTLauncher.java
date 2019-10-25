import java.io.*;

public class SetBSTLauncher {
    private static final String PATTERN = "[a-zA-Z0-9]+";
    public static void main(String[] args) {
        SetBST s1 = new SetBST();
        System.out.println("---------Part 1: Insert to the Set-----------------------");
        String pathname = "pride-and-prejudice.txt";
        try (FileReader reader = new FileReader(pathname);
             BufferedReader br = new BufferedReader(reader) // 建立一个对象，它把文件内容转成计算机能读懂的语言
        ) {
            String line;
            while ((line = br.readLine()) != null) {
                // 一次读入一行数据
                if(line.length()==0){
                    continue;
                }
                String[] words = line.split("[^a-zA-Z0-9]");
                for(String word :words){
                    long startTime = System.nanoTime();
                    boolean added = s1.add(word);
                    long endTime = System.nanoTime();

                    if (added) {
                        long duration = endTime - startTime;
                        String num = String.valueOf(duration);
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
            String line;
            while ((line = br.readLine()) != null) {
                // 一次读入一行数据
                if(line.length()==0){
                    continue;
                }
                String[] words = line.split("[^a-zA-Z0-9]");
                for(String word :words){
                    long startTime = System.nanoTime();
                    boolean contain = s1.contains(word);
                    long endTime = System.nanoTime();

                    if (!contain) {
                        notinclude += 1;
                        String num = String.valueOf(startTime-endTime);
                        writeFile("search.txt", num);
                    }
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
    private static String readFile(String fileName) {
        StringBuilder stringBuilder = new StringBuilder();
        File file = new File(fileName);
        Reader reader;
        try {
            // 一次读一个字符
            reader = new InputStreamReader(new FileInputStream(file));
            int tempchar;
            while ((tempchar = reader.read()) != -1) {
                if (!((char) tempchar+"").matches(PATTERN)) {
                    tempchar = ' ';
                }
                stringBuilder.append((char)tempchar);
            }
            reader.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
        return stringBuilder.toString();
    }

}
