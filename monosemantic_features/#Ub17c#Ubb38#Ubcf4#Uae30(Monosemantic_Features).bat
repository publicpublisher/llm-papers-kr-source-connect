@echo off
chcp 65001 >nul
echo ========================================================
echo 완벽한 오프라인 구동을 위해 로컬 임시 서버를 시작합니다...
echo 논문 열람이 끝나면 이 검은색 창을 닫아주세요.
echo ========================================================
start http://localhost:8080/2023/monosemantic-features/index.html
cd "%~dp0"
python -m http.server 8080
pause
