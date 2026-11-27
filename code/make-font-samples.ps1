# Draws one Arabic heading per installed Arabic font, as transparent PNGs, for the font test (T26).
# Example: .\make-font-samples.ps1 -Text 'عنوان مشروعي' -Fonts 'Segoe UI','Tahoma' -Color 2F81F7 -Out .\pictures
param(
  [string]$Out = "$PSScriptRoot\..\tests\fonts",
  [string]$Text = 'البدء السريع: اقرأ الدليل وافحص ملفك',
  [string[]]$Fonts = @('Aldhabi','Andalus','Arabic Typesetting','Sakkal Majalla','Simplified Arabic','Traditional Arabic','Segoe UI','Tahoma'),
  [ValidateSet('neutral','dark','light')][string[]]$Themes = @('neutral'),
  [string]$Color      # a hex colour such as 2F81F7; replaces -Themes with one picture in that colour
)
Add-Type -AssemblyName System.Drawing
New-Item -ItemType Directory -Force $Out | Out-Null
# neutral (GitHub blue) reads on dark and light pages and is the one the phone app can show; dark/light are for <picture>.
$colors = @{ dark = [System.Drawing.Color]::FromArgb(230,237,243); light = [System.Drawing.Color]::FromArgb(31,35,40); neutral = [System.Drawing.Color]::FromArgb(47,129,247) }
$use = $Themes
if ($Color) {
  $colors['custom'] = [System.Drawing.ColorTranslator]::FromHtml('#' + $Color.TrimStart('#'))
  $use = @('custom')
}
foreach ($f in $Fonts) {
  $font = New-Object System.Drawing.Font($f, 40, [System.Drawing.FontStyle]::Regular, [System.Drawing.GraphicsUnit]::Pixel)
  if ($font.Name -ne $f) {
    # Windows quietly swaps in another font when this one is not installed: skip it instead of saving a wrong picture.
    Write-Warning "Font '$f' is not installed (Windows would use '$($font.Name)'): skipped"
    $font.Dispose(); continue
  }
  $fmt = New-Object System.Drawing.StringFormat([System.Drawing.StringFormatFlags]::DirectionRightToLeft)
  $probe = New-Object System.Drawing.Bitmap(10,10); $g0 = [System.Drawing.Graphics]::FromImage($probe)
  $size = $g0.MeasureString($Text, $font, 2000, $fmt); $g0.Dispose(); $probe.Dispose()
  $w = [int][math]::Ceiling($size.Width) + 8; $h = [int][math]::Ceiling($size.Height) + 8
  foreach ($t in $use) {
    $bmp = New-Object System.Drawing.Bitmap($w, $h)
    $g = [System.Drawing.Graphics]::FromImage($bmp)
    $g.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::AntiAliasGridFit
    $g.Clear([System.Drawing.Color]::Transparent)
    $brush = New-Object System.Drawing.SolidBrush($colors[$t])
    $g.DrawString($Text, $font, $brush, (New-Object System.Drawing.RectangleF(4,4,($w-8),($h-8))), $fmt)
    $name = ($f -replace ' ','-').ToLower()
    $bmp.Save("$Out\font-$name-$t.png", [System.Drawing.Imaging.ImageFormat]::Png)
    $g.Dispose(); $bmp.Dispose(); $brush.Dispose()
  }
  $font.Dispose()
}
Get-ChildItem $Out | Select-Object Name, Length | Format-Table -HideTableHeaders
