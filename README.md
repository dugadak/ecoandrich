# 사용 인스턴스 주소
- 인스턴스 주소: [3.112.204.148](http://3.112.204.148)

# 관련 문서 및 사용법 엔드포인트
- Swagger 문서: [3.112.204.148/swagger](http://3.112.204.148/swagger)
- ReDoc 문서: [3.112.204.148/redoc](http://3.112.204.148/redoc)

# 기능 목록
1. 특정 사원의 현재 정보 조회 가능한 API 구현(GET /employees)
2. 특정 사원의 이력 정보 조회 가능한 API 구현(GET /employees/{employee_id}/history)
3. 부서 및 위치 정보 조회 가능한 API 구현(GET - 부서별 /departments GET - 위치별 /locations)
4. 특정 부서의 급여를 특정 비율로 인상 API 구현(PATCH /departments/{department_id}/salary)
   - body 예시: `{"percent" : 10}` (급여 인상)
   - body 예시: `{"percent" : -10}` (급여 삭감)
5. 사원 정보 업데이트 할 수 있는 API 구현(PATCH /employees/{employee_id})
6. 기타 각 API의 CRUD 메소드 등 다수 API 제공

# 구동 방법
1. `secret_settings.py` 파일이 필요합니다.
2. 해당 파일은 별도 메일로 발송되었습니다.

# 문의
- 추가 문의나 지원이 필요한 경우 [support@example.com](mailto:support@example.com)로 연락 바랍니다.
