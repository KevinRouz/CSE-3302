//Kevin Farokhrouz
//1002072886
//Java 1.8.0_412 (Object Oriented language)
//Win 11

import java.io.File;

public class kaf2886_lab01{
	
	//Returns the file size in bytes
	public static long getSize(File file) {
		return file.length();
	}
	
	public static long direcSize(File folder) {
		long sum = 0;
		//Lists the contents of the folder. This includes subfolders and files.
		String contents[] = folder.list();

		//Error Handling
		if (contents == null) {
			return 0;
		}
		
		for(int i = 0; i < contents.length; i++) {
			// Skip "." and ".."
			if (contents[i].equals(".") || contents[i].equals("..")) {
				continue;
			}
			//The entry path is constructed using the parent folder + entryName
			File entry = new File(folder + "/" + contents[i]);
			//Recurse through the entry if it is a subfolder
			if(entry.isDirectory()){
				sum = sum + direcSize(entry);		
			}
			else {
				//Else (the entry is a file), increment sum by the file size in bytes.
				sum = sum + getSize(entry);
			}	
		}
		return sum;
	}

	public static void main(String args[]) {
		//Functions take type File as input, format the path as a File
		File cwd = new File(".");
		//Int might not be enough for large folders. If your folder size doesn't fit inside of a long, god help you.
		long sum = direcSize(cwd);
		System.out.println(sum);	
	}
}