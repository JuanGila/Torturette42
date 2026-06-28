$image = ".\assets\TorturetteBanner1.png"

$formats = @(
    "ascii",
    "block",
    "braille",
    "dots",
    "stipple",
    "quadrant",
    "half",
    "sextant"
)

$filesfolder = Get-ChildItem -Path ".\assets\frames"

foreach ($file in $filesfolder)
{
    $outfile = ".\assets\ansi\$($file.BaseName).ansi"
    chafa $file.FullName --symbols block --colors 256 --size 120x50 --optimize 9 > $outfile
    Write-Host "Generated $outfile"
}