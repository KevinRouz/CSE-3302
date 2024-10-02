//Kevin Farokhrouz
//1002072886
//C C99 (Procedural Language)
//Win 11

#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <string.h>
#include <sys/stat.h>

//Returns the size of a file in bytes
long getSize(const char *filePath){
    //Opens the file for reading in binary mode.
    FILE *file = fopen(filePath, "rb");

    //Find the end of the file.
    fseek(file, 0, SEEK_END);

    //The end of the file is the number of bytes in the file, since we opened in rb.
    long fileSize = ftell(file);
    fclose(file);

    return fileSize;

}


unsigned long long directorySize(const char *folder){
    //We are using stat and DirEnt to help us with folder and directory checks.
    DIR * dir;
    struct dirent * entry;
    struct stat pathStat;

    //If this isn't enough space I don't know what to tell you...
    unsigned long long sum = 0;

    dir = opendir(folder);

    while((entry = readdir(dir)) != NULL){
        //Skip .. and .
        if (strcmp(entry->d_name, ".") == 0 || strcmp(entry->d_name, "..") == 0) {
            continue;
        }

        //Put the new path (folder/entryname) into a buffer
        char newPath[1024];
        snprintf(newPath, sizeof(newPath), "%s/%s", folder, entry->d_name);

        //Error handling
        if (stat(newPath, &pathStat) == -1) {
            continue;
        }

        //If entry is a directory, recurse and add the sum of those file sizes.
        if (S_ISDIR(pathStat.st_mode)){
            sum  += directorySize(newPath);
        } else{
            //Otherwise just increment sum by the size of the file.
            sum += getSize(newPath);
        }
    }

    //Never forget to close what you open. Donna French would be proud of me.
    closedir(dir);
    return sum;
}


int main(void){
    const char *cwd = ".";
    unsigned long long sum = directorySize(cwd);
    printf("%llu\n", sum);
    return 0;
}