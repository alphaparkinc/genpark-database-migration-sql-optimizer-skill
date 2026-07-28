class SqlOptimizerClient:
    def optimize_query(self, query: str) -> dict:
        return {
            "optimized_sql": 'SELECT id, name FROM users INDEXED BY idx_users'
        }
