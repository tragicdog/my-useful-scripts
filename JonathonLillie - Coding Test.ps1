$JSONFile = Get-Content "employees.json" | ConvertFrom-Json
$EmployeeCSV = Import-Csv "engineering.csv" #| ConvertFrom-Csv

#write out headers for totp_disabled csv
$totp_disabled = "firstName,lastName,email,username,jobTitle,totp_enabled,manager`n"

foreach ($PSItem in $JSONFile){
    if ($_.totp_enabled -match "False"){
        $totp_disabled += "$($_.firstName),$($_.lastName),$($_.email),$($_.username),$($_.jobTitle),$($_.totp_enabled),`n"
      }
    }

$totp_disabled | ConvertTo-Csv 
$totp_disabled | Out-File "TOTP_Disabled.csv"

$totp_disabled = Import-Csv "TOTP_Disabled.csv"

$usersInBoth = Compare-Object -ReferenceObject $EmployeeCSV.email -DifferenceObject $totp_disabled.email -IncludeEqual |where-Object {$_.SideIndicator -eq "=="} |Select-Object -ExpandProperty InputObject 

$results = ForEach($user in $usersInBoth) {
    $e = $EmployeeCSV | Where-Object {$_.email -eq $user}
    $t = $totp_disabled | Where-Object {$_.email -eq $user}

    $properties = [ordered]@{
        firstName = $e.firstName
        lastName = $e.lastName
        email = $t.email
        username = $t.username 
        manager = $e.manager
        jobTitle = $t.jobTitle
    }

    New-Object -TypeName psobject -Property $properties
}

$results | Export-CSV -NoTypeInformation -Path 'TOTP_Disabled.csv'