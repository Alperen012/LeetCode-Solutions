double average(int* salary, int salarySize){
    int min=salary[0];
    int max=0;
    double t=0;
    int i=0;
    for (i=0;i<salarySize;i++)
    {
        if (max<=salary[i]){max=salary[i];}
        if (min>=salary[i]){min=salary[i];}
        t=t+salary[i];
    }

    return (t-max-min)/(salarySize-2);


}