# Builds the 1200x630 social share card for Dick's Pawn Superstore.
# Uses their real logo + real product photography from the live catalog.
Add-Type -AssemblyName System.Drawing

$dir  = "C:\Users\kylef\AppData\Local\Temp\claude\C--Users-kylef-Downloads-New-folder\3735687f-b866-4fde-bbaf-04ef4248bd40\scratchpad\og"
$site = "C:\Users\kylef\Downloads\New folder\dicks-pawn-redesign"
$W = 1200; $H = 630

$bmp = New-Object System.Drawing.Bitmap($W, $H)
$g   = [System.Drawing.Graphics]::FromImage($bmp)
$g.SmoothingMode     = [System.Drawing.Drawing2D.SmoothingMode]::AntiAlias
$g.InterpolationMode = [System.Drawing.Drawing2D.InterpolationMode]::HighQualityBicubic
$g.TextRenderingHint = [System.Drawing.Text.TextRenderingHint]::ClearTypeGridFit

# ---- background: navy gradient ----
$rect = New-Object System.Drawing.Rectangle(0, 0, $W, $H)
$brush = New-Object System.Drawing.Drawing2D.LinearGradientBrush(
  $rect,
  [System.Drawing.Color]::FromArgb(8, 26, 51),
  [System.Drawing.Color]::FromArgb(29, 74, 138),
  [System.Drawing.Drawing2D.LinearGradientMode]::ForwardDiagonal)
$g.FillRectangle($brush, $rect)

# soft red glow bottom-left (matches the site's hero)
$glow = New-Object System.Drawing.Drawing2D.GraphicsPath
$glow.AddEllipse(-260, 380, 780, 620)
$pgb = New-Object System.Drawing.Drawing2D.PathGradientBrush($glow)
$pgb.CenterColor = [System.Drawing.Color]::FromArgb(70, 193, 39, 45)
$pgb.SurroundColors = @([System.Drawing.Color]::FromArgb(0, 193, 39, 45))
$g.FillPath($pgb, $glow)

function New-RoundedPath($x, $y, $w, $h, $r) {
  $p = New-Object System.Drawing.Drawing2D.GraphicsPath
  $d = $r * 2
  $p.AddArc($x, $y, $d, $d, 180, 90)
  $p.AddArc($x + $w - $d, $y, $d, $d, 270, 90)
  $p.AddArc($x + $w - $d, $y + $h - $d, $d, $d, 0, 90)
  $p.AddArc($x, $y + $h - $d, $d, $d, 90, 90)
  $p.CloseFigure()
  return $p
}

# ---- product tile grid (right side) ----
$tile = 186; $gap = 14
$gridW = $tile * 2 + $gap
$gx = $W - 56 - $gridW
$gy = ($H - ($tile * 3 + $gap * 2)) / 2
$white = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::White)

$order = @(9, 3, 2, 4, 1, 7)   # diamond ring, jordan, guitar, LV bag, PS5, golf
$i = 0
foreach ($n in $order) {
  $f = Join-Path $dir "p$n.jpg"
  if (-not (Test-Path $f)) { $f = Join-Path $dir "p$n.png" }
  if (-not (Test-Path $f)) { continue }
  $col = $i % 2; $row = [math]::Floor($i / 2)
  $x = $gx + $col * ($tile + $gap)
  $y = $gy + $row * ($tile + $gap)

  $path = New-RoundedPath $x $y $tile $tile 16
  $g.FillPath($white, $path)          # white card behind the product shot

  $img = [System.Drawing.Image]::FromFile($f)
  # contain-fit the photo inside the tile with a small inset
  $inset = 10
  $avail = $tile - $inset * 2
  $scale = [math]::Min($avail / $img.Width, $avail / $img.Height)
  $dw = [int]($img.Width * $scale); $dh = [int]($img.Height * $scale)
  $dx = $x + ($tile - $dw) / 2; $dy = $y + ($tile - $dh) / 2

  $state = $g.Save()
  $g.SetClip($path)
  $g.DrawImage($img, $dx, $dy, $dw, $dh)
  $g.Restore($state)
  $img.Dispose()
  $i++
}

# ---- logo ----
$logoFile = Join-Path $site "assets\dp-logo.png"
$logo = [System.Drawing.Image]::FromFile($logoFile)
$lw = 104; $lh = [int]($logo.Height * ($lw / $logo.Width))
$g.DrawImage($logo, 60, 54, $lw, $lh)
$logo.Dispose()

# ---- type ----
function Get-Font($name, $size, $style) {
  foreach ($n in @($name, 'Segoe UI', 'Arial')) {
    try { return New-Object System.Drawing.Font($n, $size, $style, [System.Drawing.GraphicsUnit]::Pixel) } catch {}
  }
}
$wordF  = Get-Font 'Jost'    26 ([System.Drawing.FontStyle]::Bold)
$estF   = Get-Font 'Jost'    15 ([System.Drawing.FontStyle]::Bold)
$headF  = Get-Font 'Jost'    54 ([System.Drawing.FontStyle]::Bold)
$subF   = Get-Font 'Jost'    23 ([System.Drawing.FontStyle]::Regular)
$chipF  = Get-Font 'Jost'    19 ([System.Drawing.FontStyle]::Bold)

$wBrush   = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::White)
$goldBr   = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(255, 209, 102))
$iceBr    = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(214, 228, 245))
$redBr    = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(230, 70, 72))

$tx = 178
$g.DrawString("DICK'S PAWN", $wordF, $wBrush, $tx, 62)
$dot = [char]0x00B7
$g.DrawString("SUPERSTORE  $dot  EST. 1987", $estF, $redBr, ($tx + 2), 96)

# headline
$g.DrawString("Why pay retail?", $headF, $wBrush, 58, 176)
$g.DrawString(("Shop 1,500+ deals " + [char]0x2014 + " or"), $headF, $wBrush, 58, 238)
$g.DrawString("get same-day cash.", $headF, $goldBr, 58, 300)

$g.DrawString("Family-owned pawn superstore on the Grand Strand.", $subF, $iceBr, 60, 382)
$g.DrawString((("Jewelry","Electronics","Instruments","Tools","Sneakers") -join (" " + [char]0x00B7 + " ")), $subF, $iceBr, 60, 414)

# ---- trust chips ----
$chips = @(([char]0x2605 + " 4.9   2,000+ Reviews"), "5 Locations", "Since 1987")
$cx = 60
foreach ($c in $chips) {
  $sz = $g.MeasureString($c, $chipF)
  $cw = [int]$sz.Width + 34
  $ch = 44
  $p = New-RoundedPath $cx 486 $cw $ch 22
  $fill = New-Object System.Drawing.SolidBrush([System.Drawing.Color]::FromArgb(38, 255, 255, 255))
  $pen  = New-Object System.Drawing.Pen([System.Drawing.Color]::FromArgb(90, 255, 255, 255), 1.5)
  $g.FillPath($fill, $p)
  $g.DrawPath($pen, $p)
  $g.DrawString($c, $chipF, $wBrush, ($cx + 17), 497)
  $cx += $cw + 12
}

# ---- domain footer ----
$domF = Get-Font 'Jost' 20 ([System.Drawing.FontStyle]::Bold)
$g.DrawString("dickspawn.com", $domF, $goldBr, 60, 556)

# ---- save ----
$out = Join-Path $site "assets\og-card.jpg"
$codec = [System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders() | Where-Object { $_.MimeType -eq 'image/jpeg' }
$ep = New-Object System.Drawing.Imaging.EncoderParameters(1)
$ep.Param[0] = New-Object System.Drawing.Imaging.EncoderParameter([System.Drawing.Imaging.Encoder]::Quality, 90)
$bmp.Save($out, $codec, $ep)
$g.Dispose(); $bmp.Dispose()

$fi = Get-Item $out
Write-Output ("saved: " + $fi.FullName)
Write-Output ("size:  " + [math]::Round($fi.Length / 1KB, 1) + " KB")
