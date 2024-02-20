from fastapi import FastAPI, Depends,status, Response, HTTPException
from .import schemas,models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session

app= FastAPI()

models.BASE.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@app.post("/blog",status_code=status.HTTP_201_CREATED)
def create_blog(request:schemas.Blog, db : Session=Depends(get_db)):
    new_blog = models.Blog(title = request.title, body = request.body)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog

@app.get("/blog_data")
def get_all_blogs(db : Session=Depends(get_db)):
    blogs= db.query(models.Blog).all()
    return blogs

@app.get("/blog_data/{id}",status_code=200)
def get_specific_blog(id,response : Response , db : Session=Depends(get_db)):
    # blog_show=db.query(models.Blog).get(id)
    blog_show=db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog_show:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Blog for requested id {id} is not found.')
        # response.status_code =  status.HTTP_404_NOT_FOUND
        # return {"detail":f'Blog for requested id {id} is not found.'}
        
    return blog_show
   
@app.delete("/blog_delete/{id}", status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db : Session=Depends(get_db)):
    db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()
    return "required data is removed"