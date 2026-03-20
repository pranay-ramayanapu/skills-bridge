import React, { useState } from "react";
import './index.css'
const ROLES = [
  { role: "Data Engineer" },
  { role: "Backend Developer" },
  { role: "Frontend Developer" },
  { role: "Full Stack Developer" },
  { role: "DevOps Engineer" },
  { role: "Machine Learning Engineer" },
  { role: "Data Analyst" },
  { role: "Cloud Engineer" },
  { role: "Software Engineer" },
  { role: "Mobile App Developer" },
  { role: "Database Administrator" },
  { role: "Cybersecurity Engineer" },
  { role: "AI Engineer" },
  { role: "QA Engineer" },
  { role: "Site Reliability Engineer" }
];

export default function ResumeAnalyzer() {
  const [text, setText] = useState("");
  const [file, setFile] = useState(null);
  const [loading, setLoading] = useState(false);
  const [selectedRole, setSelectedRole] = useState("");

  const [skillsHave, setSkillsHave] = useState([]);
  const [skillsRequired, setSkillsRequired] = useState([]);
  const [roadmap, setRoadmap] = useState({});

  const handleSubmit = async () => {
    setLoading(true);

    const formData = new FormData();
    formData.append("resume_text", text);
    formData.append("role", selectedRole); // <-- YOU FORGOT THIS
    if (file) formData.append("file", file);
    if (!selectedRole) {
      alert("Please select a role");
      return;
    }

    try {
      const res = await fetch("http://localhost:8000/analyze", {
        method: "POST",
        body: formData,
      });

      const data = await res.json();

      setSkillsHave(data.extracted_skills || []);
      setSkillsRequired(data.missing_skills || []);
      const groupRoadmap = (data) => {
        const grouped = {};

        data.forEach((item) => {
          if (!grouped[item.skill]) {
            grouped[item.skill] = [];
          }
          grouped[item.skill].push(item);
        });

        return grouped;
      };
      setRoadmap(groupRoadmap(data.roadmap || []));
    } catch (err) {
      console.error(err);
    }

    setLoading(false);
  };
  console.log("ROADMAP:", roadmap);

  return (
    <div className="min-h-screen bg-gray-100 p-6">
      {/* SECTION 1: INPUT */}
      <div className="bg-white shadow-lg rounded-2xl p-6 mb-6">
        <h1 className="text-2xl font-bold mb-4">
          Resume Skill Analyzer
        </h1>

        <textarea
          placeholder="Paste your resume here..."
          className="w-full h-40 border rounded-lg p-3 mb-4"
          value={text}
          onChange={(e) => setText(e.target.value)}
        />

        <div className="flex items-center gap-4 mb-4">
          <input
            type="file"
            onChange={(e) => setFile(e.target.files[0])}
          />
          <span className="text-sm text-gray-500">
            Upload PDF / DOCX
          </span>
        </div>
        <select
          className="w-full border rounded-lg p-3 mb-4"
          value={selectedRole}
          onChange={(e) => setSelectedRole(e.target.value)}
        >
          <option value="">Select Target Role</option>
          {ROLES.map((r, idx) => (
            <option key={idx} value={r.role}>
              {r.role}
            </option>
          ))}
        </select>

        <button
          onClick={handleSubmit}
          className="bg-blue-600 text-white px-6 py-2 rounded-lg hover:bg-blue-700"
        >
          {loading ? "Processing..." : "Analyze Resume"}
        </button>
      </div>

      {/* SECTION 2: SKILLS */}
      <div className="grid md:grid-cols-2 gap-6 mb-6">
        {/* Skills Have */}
        <div className="bg-white shadow rounded-2xl p-5">
          <h2 className="text-xl font-semibold mb-3 text-green-600">
            Skills You Have
          </h2>

          <div className="flex flex-wrap gap-2">
            {skillsHave.map((skill, index) => (
              <span
                key={index}
                className="bg-green-100 text-green-700 px-3 py-1 rounded-full text-sm"
              >
                {skill}
              </span>
            ))}
          </div>
        </div>

        {/* Skills Required */}
        <div className="bg-white shadow rounded-2xl p-5">
          <h2 className="text-xl font-semibold mb-3 text-red-600">
            Skills Required
          </h2>

          <div className="flex flex-wrap gap-2">
            {skillsRequired.map((skill, index) => (
              <span
                key={index}
                className="bg-red-100 text-red-700 px-3 py-1 rounded-full text-sm"
              >
                {skill}
              </span>
            ))}
          </div>
        </div>
      </div>

      {/* SECTION 3: ROADMAP */}
      <div className="bg-white shadow-lg rounded-2xl p-6">
        <h2 className="text-xl font-semibold mb-4">
          Learning Roadmap
        </h2>

        <div className="grid md:grid-cols-2 gap-6">
          {Object.keys(roadmap).map((skill, idx) => (
            <div
              key={idx}
              className="border rounded-xl p-4 hover:shadow-md"
            >
              <h3 className="font-bold mb-2 capitalize">
                {skill}
              </h3>

              {roadmap[skill].map((course, i) => (
                <div
                  key={i}
                  className="mb-2 p-2 bg-gray-50 rounded-lg"
                >
                  <p className="font-medium">{course.title}</p>
                  <p className="text-sm text-gray-500">
                    {course.duration} • {course.type}
                  </p>
                </div>
              ))}
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
