Import-Excel -Path "C:\Users\ezrab\OneDrive\Documents\TestData.xlsx" | Export-Csv -Path "C:\Users\ezrab\OneDrive\Documents\TestData.csv" -NoTypeInformation

$Files = Get-ChildItem -Path "C:\Users\ezrab\OneDrive\Documents" -Include *.xlsx -Recurse
ForEach ($File in $Files)
{
    Import-Excel -Path $File.FullName | Export-Csv ($file.FullName -replace '\.xlsx', '.csv')
}