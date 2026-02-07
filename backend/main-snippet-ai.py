from database import database, circuits, components, ai_courses, metadata

class AICourseRequest(BaseModel):
    title: str
    description: Optional[str] = None
    week: Optional[int] = None
    content: Optional[str] = None
    image_url: Optional[Union[str, List[str]]] = None

class AICourseResponse(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    week: Optional[int] = None
    content: Optional[str] = None
    image_url: Optional[Union[str, List[str]]] = None
    created_at: datetime

@app.get("/api/ai-courses", response_model=list[AICourseResponse])
async def get_ai_courses():
    query = ai_courses.select().order_by(ai_courses.c.week)
    results = await database.fetch_all(query)
    return [dict(r) for r in results]

@app.post("/api/ai-courses", response_model=AICourseResponse)
async def create_ai_course(request: AICourseRequest):
    try:
        query = ai_courses.insert().values(
            title=request.title,
            description=request.description,
            week=request.week,
            content=request.content,
            image_url=request.image_url,
            created_at=datetime.utcnow()
        )
        last_record_id = await database.execute(query)
        return {
            **request.dict(),
            "id": last_record_id,
            "created_at": datetime.utcnow()
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.put("/api/ai-courses/{course_id}", response_model=AICourseResponse)
async def update_ai_course(course_id: int, request: AICourseRequest):
    try:
        query = ai_courses.update().where(ai_courses.c.id == course_id).values(
            title=request.title,
            description=request.description,
            week=request.week,
            content=request.content,
            image_url=request.image_url
        )
        await database.execute(query)
        
        fetch_query = ai_courses.select().where(ai_courses.c.id == course_id)
        result = await database.fetch_one(fetch_query)
        if not result:
             raise HTTPException(status_code=404, detail="Course module not found")
        return dict(result)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.delete("/api/ai-courses/{course_id}")
async def delete_ai_course(course_id: int):
    query = ai_courses.delete().where(ai_courses.c.id == course_id)
    await database.execute(query)
    return {"message": "Course module deleted successfully"}
