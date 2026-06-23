'use client';

import { useEffect, useState } from 'react';
import { apiService } from '@/lib/api';
import { 
  TaskView, 
  User, 
  Category, 
  Priority, 
  Progress, 
  Material,
  CreateTask
} from '@/lib/types';
import { 
  Plus, 
  Trash2, 
  User as UserIcon, 
  CheckCircle, 
  Clock, 
  Tag, 
  AlertCircle,
  Package,
  X
} from 'lucide-react';

export default function Home() {
  const [tasks, setTasks] = useState<TaskView[]>([]);
  const [users, setUsers] = useState<User[]>([]);
  const [categories, setCategories] = useState<Category[]>([]);
  const [priorities, setPriorities] = useState<Priority[]>([]);
  const [progresses, setProgresses] = useState<Progress[]>([]);
  const [materials, setMaterials] = useState<Material[]>([]);
  
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);
  const [activeTab, setActiveTab] = useState<'tasks' | 'users' | 'settings'>('tasks');

  // Form states
  const [showTaskForm, setShowTaskForm] = useState(false);
  const [showUserForm, setShowUserForm] = useState(false);
  const [showCategoryForm, setShowCategoryForm] = useState(false);
  const [showMaterialForm, setShowMaterialForm] = useState(false);

  const [newTask, setNewTask] = useState<Partial<CreateTask>>({
    Titel: '',
    Notiz: '',
    Ort: '',
    Beginn: new Date().toISOString().split('T')[0],
    Ende: new Date().toISOString().split('T')[0],
    KategorieID: 1,
    PrioritaetID: 1,
    FortschrittID: 1,
    BenutzerID: 1
  });

  const [newUser, setNewUser] = useState({ BenutzerName: '', BenutzerPWD: '' });
  const [newCategory, setNewCategory] = useState({ Kategorie: '', IstAktiv: true });
  const [newMaterial, setNewMaterial] = useState({ Material: '', IstAktiv: true });

  const fetchData = async () => {
    try {
      setLoading(true);
      const [
        tasksData, 
        usersData, 
        categoriesData, 
        prioritiesData, 
        progressData, 
        materialsData
      ] = await Promise.all([
        apiService.getTaskViews(),
        apiService.getUsers(),
        apiService.getCategories(),
        apiService.getPriorities(),
        apiService.getProgress(),
        apiService.getMaterials(),
      ]);
      setTasks(tasksData);
      setUsers(usersData);
      setCategories(categoriesData);
      setPriorities(prioritiesData);
      setProgresses(progressData);
      setMaterials(materialsData);
      
      // Initialize form with first available IDs if they exist
      if (usersData.length > 0) setNewTask(prev => ({ ...prev, BenutzerID: usersData[0].BenutzerID }));
      if (categoriesData.length > 0) setNewTask(prev => ({ ...prev, KategorieID: categoriesData[0].KategorieID }));
      if (prioritiesData.length > 0) setNewTask(prev => ({ ...prev, PrioritaetID: prioritiesData[0].PrioritaetID }));
      if (progressData.length > 0) setNewTask(prev => ({ ...prev, FortschrittID: progressData[0].FortschrittID }));

    } catch (err) {
      console.error('Failed to fetch data:', err);
      setError('Verbindung zum Backend fehlgeschlagen. Stelle sicher, dass es auf https://shading-crave-preacher.ngrok-free.dev läuft');
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchData();
  }, []);

  const handleCreateTask = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await apiService.createTask(newTask as CreateTask);
      setShowTaskForm(false);
      fetchData();
    } catch (err) {
      alert('Aufgabe konnte nicht erstellt werden');
    }
  };

  const handleCreateUser = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await apiService.createUser(newUser);
      setShowUserForm(false);
      setNewUser({ BenutzerName: '', BenutzerPWD: '' });
      fetchData();
    } catch (err) {
      alert('Benutzer konnte nicht erstellt werden');
    }
  };

  const handleCreateCategory = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await apiService.createCategory(newCategory);
      setShowCategoryForm(false);
      setNewCategory({ Kategorie: '', IstAktiv: true });
      fetchData();
    } catch (err) {
      alert('Kategorie konnte nicht erstellt werden');
    }
  };

  const handleCreateMaterial = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      await apiService.createMaterial(newMaterial);
      setShowMaterialForm(false);
      setNewMaterial({ Material: '', IstAktiv: true });
      fetchData();
    } catch (err) {
      alert('Material konnte nicht erstellt werden');
    }
  };

  const handleDeleteTask = async (id: number) => {
    if (confirm('Bist du sicher, dass du diese Aufgabe löschen möchtest?')) {
      try {
        await apiService.deleteTask(id);
        fetchData();
      } catch (err) {
        alert('Aufgabe konnte nicht gelöscht werden');
      }
    }
  };

  const handleDeleteUser = async (id: number) => {
    if (confirm('Bist du sicher, dass du diesen Benutzer löschen möchtest?')) {
      try {
        await apiService.deleteUser(id);
        fetchData();
      } catch (err) {
        alert('Benutzer konnte nicht gelöscht werden. Möglicherweise sind ihm noch Aufgaben zugewiesen.');
      }
    }
  };

  const handleDeleteCategory = async (id: number) => {
    if (confirm('Bist du sicher, dass du diese Kategorie löschen möchtest?')) {
      try {
        await apiService.deleteCategory(id);
        fetchData();
      } catch (err) {
        alert('Kategorie konnte nicht gelöscht werden');
      }
    }
  };

  const handleDeleteMaterial = async (id: number) => {
    if (confirm('Bist du sicher, dass du dieses Material löschen möchtest?')) {
      try {
        await apiService.deleteMaterial(id);
        fetchData();
      } catch (err) {
        alert('Material konnte nicht gelöscht werden');
      }
    }
  };

  const handleUpdateStatus = async (taskId: number, statusId: number) => {
    try {
      await apiService.updateTaskStatus(taskId, statusId);
      fetchData();
    } catch (err) {
      alert('Status konnte nicht aktualisiert werden');
    }
  };

  if (loading && tasks.length === 0) {
    return <div className="flex items-center justify-center min-h-screen">Anwendung wird geladen...</div>;
  }

  return (
    <div className="min-h-screen bg-zinc-50 dark:bg-black text-zinc-900 dark:text-zinc-100 p-4 md:p-8">
      <header className="max-w-6xl mx-auto mb-8 flex flex-col md:flex-row md:items-center justify-between gap-4">
        <div>
          <h1 className="text-3xl font-bold tracking-tight">AufgabenPlaner</h1>
          <p className="text-zinc-500">Alles an einem Ort verwalten</p>
        </div>
        
        <nav className="flex bg-zinc-200 dark:bg-zinc-800 p-1 rounded-lg">
          <button 
            onClick={() => setActiveTab('tasks')}
            className={`px-4 py-2 rounded-md transition-all ${activeTab === 'tasks' ? 'bg-white dark:bg-zinc-700 shadow-sm' : 'hover:opacity-70'}`}
          >
            Aufgaben
          </button>
          <button 
            onClick={() => setActiveTab('users')}
            className={`px-4 py-2 rounded-md transition-all ${activeTab === 'users' ? 'bg-white dark:bg-zinc-700 shadow-sm' : 'hover:opacity-70'}`}
          >
            Benutzer
          </button>
          <button 
            onClick={() => setActiveTab('settings')}
            className={`px-4 py-2 rounded-md transition-all ${activeTab === 'settings' ? 'bg-white dark:bg-zinc-700 shadow-sm' : 'hover:opacity-70'}`}
          >
            Einstellungen
          </button>
        </nav>
      </header>

      <main className="max-w-6xl mx-auto">
        {error && (
          <div className="mb-6 p-4 bg-red-100 border border-red-200 text-red-700 rounded-lg flex items-center gap-2">
            <AlertCircle size={20} />
            {error}
          </div>
        )}

        {/* TASKS VIEW */}
        {activeTab === 'tasks' && (
          <section>
            <div className="flex justify-between items-center mb-6">
              <h2 className="text-2xl font-semibold">Aktuelle Aufgaben</h2>
              <button 
                onClick={() => setShowTaskForm(true)}
                className="flex items-center gap-2 bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg transition-colors"
              >
                <Plus size={20} /> Neue Aufgabe
              </button>
            </div>

            <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
              {tasks.length === 0 ? (
                <div className="col-span-full py-12 text-center border-2 border-dashed rounded-xl text-zinc-500">
                  Keine Aufgaben gefunden. Erstelle deine erste Aufgabe!
                </div>
              ) : (
                tasks.map((task) => (
                  <div key={task.AufgabeID} className="bg-white dark:bg-zinc-900 border rounded-xl p-5 shadow-sm">
                    <div className="flex justify-between items-start mb-4">
                      <div>
                        <h3 className="text-xl font-bold mb-1">{task.Titel}</h3>
                        <div className="flex flex-wrap gap-2">
                          <span className="flex items-center gap-1 text-xs bg-zinc-100 dark:bg-zinc-800 px-2 py-1 rounded">
                            <Tag size={12} /> {task.Kategorie}
                          </span>
                          <span className="flex items-center gap-1 text-xs bg-zinc-100 dark:bg-zinc-800 px-2 py-1 rounded">
                            <AlertCircle size={12} /> {task.Prioritaet}
                          </span>
                        </div>
                      </div>
                      <button 
                        onClick={() => handleDeleteTask(task.AufgabeID)}
                        className="text-zinc-400 hover:text-red-500 p-1"
                      >
                        <Trash2 size={18} />
                      </button>
                    </div>

                    <p className="text-zinc-600 dark:text-zinc-400 text-sm mb-4 min-h-[3rem]">
                      {task.Notiz || 'Keine Beschreibung vorhanden.'}
                    </p>

                    <div className="flex items-center justify-between pt-4 border-t text-sm text-zinc-500">
                      <div className="flex items-center gap-3">
                        <span title="Ort">📍 {task.Ort}</span>
                        <span title="Zugewiesener Benutzer" className="flex items-center gap-1">
                          <UserIcon size={14} /> {task.BenutzerName}
                        </span>
                      </div>
                      
                      <select 
                        value={progresses.find(p => p.Fortschritt === task.Fortschritt)?.FortschrittID || 1}
                        onChange={(e) => handleUpdateStatus(task.AufgabeID, parseInt(e.target.value))}
                        className="bg-zinc-100 dark:bg-zinc-800 border-none rounded px-2 py-1 text-xs focus:ring-1 focus:ring-blue-500"
                      >
                        {progresses.map(p => (
                          <option key={p.FortschrittID} value={p.FortschrittID}>{p.Fortschritt}</option>
                        ))}
                      </select>
                    </div>
                  </div>
                ))
              )}
            </div>
          </section>
        )}

        {/* USERS VIEW */}
        {activeTab === 'users' && (
          <section>
            <div className="flex justify-between items-center mb-6">
              <h2 className="text-2xl font-semibold">Benutzerverwaltung</h2>
              <button 
                onClick={() => setShowUserForm(true)}
                className="flex items-center gap-2 bg-blue-600 hover:bg-blue-700 text-white px-4 py-2 rounded-lg transition-colors"
              >
                <Plus size={20} /> Neuer Benutzer
              </button>
            </div>
            <div className="bg-white dark:bg-zinc-900 border rounded-xl overflow-hidden">
              <table className="w-full text-left">
                <thead className="bg-zinc-50 dark:bg-zinc-800/50">
                  <tr>
                    <th className="px-6 py-3 text-sm font-medium">ID</th>
                    <th className="px-6 py-3 text-sm font-medium">Benutzername</th>
                    <th className="px-6 py-3 text-sm font-medium text-right">Aktionen</th>
                  </tr>
                </thead>
                <tbody className="divide-y">
                  {users.map(user => (
                    <tr key={user.BenutzerID}>
                      <td className="px-6 py-4 text-sm text-zinc-500">{user.BenutzerID}</td>
                      <td className="px-6 py-4 font-medium">{user.BenutzerName}</td>
                      <td className="px-6 py-4 text-right">
                        <button 
                          onClick={() => handleDeleteUser(user.BenutzerID)}
                          className="text-zinc-400 hover:text-red-500"
                        >
                          <Trash2 size={18} />
                        </button>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
          </section>
        )}

        {/* SETTINGS VIEW (Categories, etc) */}
        {activeTab === 'settings' && (
          <section className="grid grid-cols-1 md:grid-cols-2 gap-8">
            <div>
              <div className="flex justify-between items-center mb-4">
                <h2 className="text-xl font-semibold flex items-center gap-2">
                  <Tag size={20} /> Kategorien
                </h2>
                <button 
                  onClick={() => setShowCategoryForm(true)}
                  className="text-blue-600 hover:text-blue-700 text-sm font-medium"
                >
                  + Hinzufügen
                </button>
              </div>
              <div className="bg-white dark:bg-zinc-900 border rounded-xl divide-y">
                {categories.map(cat => (
                  <div key={cat.KategorieID} className="p-4 flex justify-between items-center">
                    <span>{cat.Kategorie}</span>
                    <div className="flex items-center gap-3">
                      <span className={`text-xs px-2 py-1 rounded ${cat.IstAktiv ? 'bg-green-100 text-green-700' : 'bg-zinc-100 text-zinc-500'}`}>
                        {cat.IstAktiv ? 'Aktiv' : 'Inaktiv'}
                      </span>
                      <button 
                        onClick={() => handleDeleteCategory(cat.KategorieID)}
                        className="text-zinc-400 hover:text-red-500"
                      >
                        <Trash2 size={16} />
                      </button>
                    </div>
                  </div>
                ))}
              </div>
            </div>

            <div>
              <div className="flex justify-between items-center mb-4">
                <h2 className="text-xl font-semibold flex items-center gap-2">
                  <Package size={20} /> Materialien
                </h2>
                <button 
                  onClick={() => setShowMaterialForm(true)}
                  className="text-blue-600 hover:text-blue-700 text-sm font-medium"
                >
                  + Hinzufügen
                </button>
              </div>
              <div className="bg-white dark:bg-zinc-900 border rounded-xl divide-y">
                {materials.map(mat => (
                  <div key={mat.MaterialID} className="p-4 flex justify-between items-center">
                    <span>{mat.Material}</span>
                    <div className="flex items-center gap-3">
                      <span className={`text-xs px-2 py-1 rounded ${mat.IstAktiv ? 'bg-green-100 text-green-700' : 'bg-zinc-100 text-zinc-500'}`}>
                        {mat.IstAktiv ? 'Verfügbar' : 'Nicht verfügbar'}
                      </span>
                      <button 
                        onClick={() => handleDeleteMaterial(mat.MaterialID)}
                        className="text-zinc-400 hover:text-red-500"
                      >
                        <Trash2 size={16} />
                      </button>
                    </div>
                  </div>
                ))}
              </div>
            </div>
          </section>
        )}
      </main>

      {/* TASK FORM MODAL */}
      {showTaskForm && (
        <div className="fixed inset-0 bg-black/50 backdrop-blur-sm flex items-center justify-center p-4 z-50">
          <div className="bg-white dark:bg-zinc-900 rounded-2xl shadow-xl w-full max-w-lg overflow-hidden">
            <div className="p-6 border-b flex justify-between items-center">
              <h3 className="text-xl font-bold">Neue Aufgabe erstellen</h3>
              <button onClick={() => setShowTaskForm(false)}><X size={24} /></button>
            </div>
            <form onSubmit={handleCreateTask} className="p-6 space-y-4">
              <div className="grid grid-cols-1 gap-4">
                <div>
                  <label className="block text-sm font-medium mb-1">Titel</label>
                  <input 
                    required
                    type="text" 
                    className="w-full bg-zinc-50 dark:bg-zinc-800 border rounded-lg px-3 py-2"
                    value={newTask.Titel}
                    onChange={e => setNewTask({...newTask, Titel: e.target.value})}
                  />
                </div>
                <div>
                  <label className="block text-sm font-medium mb-1">Notiz</label>
                  <textarea 
                    className="w-full bg-zinc-50 dark:bg-zinc-800 border rounded-lg px-3 py-2"
                    value={newTask.Notiz}
                    onChange={e => setNewTask({...newTask, Notiz: e.target.value})}
                  />
                </div>
                <div className="grid grid-cols-2 gap-4">
                  <div>
                    <label className="block text-sm font-medium mb-1">Ort</label>
                    <input 
                      type="text" 
                      className="w-full bg-zinc-50 dark:bg-zinc-800 border rounded-lg px-3 py-2"
                      value={newTask.Ort}
                      onChange={e => setNewTask({...newTask, Ort: e.target.value})}
                    />
                  </div>
                  <div>
                    <label className="block text-sm font-medium mb-1">Benutzer</label>
                    <select 
                      className="w-full bg-zinc-50 dark:bg-zinc-800 border rounded-lg px-3 py-2"
                      value={newTask.BenutzerID}
                      onChange={e => setNewTask({...newTask, BenutzerID: parseInt(e.target.value)})}
                    >
                      {users.map(u => <option key={u.BenutzerID} value={u.BenutzerID}>{u.BenutzerName}</option>)}
                    </select>
                  </div>
                </div>
                <div className="grid grid-cols-3 gap-4">
                  <div>
                    <label className="block text-sm font-medium mb-1">Kategorie</label>
                    <select 
                      className="w-full bg-zinc-50 dark:bg-zinc-800 border rounded-lg px-3 py-2"
                      value={newTask.KategorieID}
                      onChange={e => setNewTask({...newTask, KategorieID: parseInt(e.target.value)})}
                    >
                      {categories.map(c => <option key={c.KategorieID} value={c.KategorieID}>{c.Kategorie}</option>)}
                    </select>
                  </div>
                  <div>
                    <label className="block text-sm font-medium mb-1">Priorität</label>
                    <select 
                      className="w-full bg-zinc-50 dark:bg-zinc-800 border rounded-lg px-3 py-2"
                      value={newTask.PrioritaetID}
                      onChange={e => setNewTask({...newTask, PrioritaetID: parseInt(e.target.value)})}
                    >
                      {priorities.map(p => <option key={p.PrioritaetID} value={p.PrioritaetID}>{p.Prioritaet}</option>)}
                    </select>
                  </div>
                  <div>
                    <label className="block text-sm font-medium mb-1">Status</label>
                    <select 
                      className="w-full bg-zinc-50 dark:bg-zinc-800 border rounded-lg px-3 py-2"
                      value={newTask.FortschrittID}
                      onChange={e => setNewTask({...newTask, FortschrittID: parseInt(e.target.value)})}
                    >
                      {progresses.map(p => <option key={p.FortschrittID} value={p.FortschrittID}>{p.Fortschritt}</option>)}
                    </select>
                  </div>
                </div>
              </div>
              <div className="pt-4">
                <button 
                  type="submit"
                  className="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 rounded-lg transition-colors"
                >
                  Aufgabe erstellen
                </button>
              </div>
            </form>
          </div>
        </div>
      )}

      {/* USER FORM MODAL */}
      {showUserForm && (
        <div className="fixed inset-0 bg-black/50 backdrop-blur-sm flex items-center justify-center p-4 z-50">
          <div className="bg-white dark:bg-zinc-900 rounded-2xl shadow-xl w-full max-w-sm overflow-hidden">
            <div className="p-6 border-b flex justify-between items-center">
              <h3 className="text-xl font-bold">Neuen Benutzer hinzufügen</h3>
              <button onClick={() => setShowUserForm(false)}><X size={24} /></button>
            </div>
            <form onSubmit={handleCreateUser} className="p-6 space-y-4">
              <div>
                <label className="block text-sm font-medium mb-1">Benutzername</label>
                <input 
                  required
                  type="text" 
                  className="w-full bg-zinc-50 dark:bg-zinc-800 border rounded-lg px-3 py-2"
                  value={newUser.BenutzerName}
                  onChange={e => setNewUser({...newUser, BenutzerName: e.target.value})}
                />
              </div>
              <div>
                <label className="block text-sm font-medium mb-1">Passwort</label>
                <input 
                  required
                  type="password" 
                  className="w-full bg-zinc-50 dark:bg-zinc-800 border rounded-lg px-3 py-2"
                  value={newUser.BenutzerPWD}
                  onChange={e => setNewUser({...newUser, BenutzerPWD: e.target.value})}
                />
              </div>
              <button 
                type="submit"
                className="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 rounded-lg transition-colors"
              >
                Benutzer erstellen
              </button>
            </form>
          </div>
        </div>
      )}

      {/* CATEGORY FORM MODAL */}
      {showCategoryForm && (
        <div className="fixed inset-0 bg-black/50 backdrop-blur-sm flex items-center justify-center p-4 z-50">
          <div className="bg-white dark:bg-zinc-900 rounded-2xl shadow-xl w-full max-w-sm overflow-hidden">
            <div className="p-6 border-b flex justify-between items-center">
              <h3 className="text-xl font-bold">Neue Kategorie</h3>
              <button onClick={() => setShowCategoryForm(false)}><X size={24} /></button>
            </div>
            <form onSubmit={handleCreateCategory} className="p-6 space-y-4">
              <div>
                <label className="block text-sm font-medium mb-1">Kategoriename</label>
                <input 
                  required
                  type="text" 
                  className="w-full bg-zinc-50 dark:bg-zinc-800 border rounded-lg px-3 py-2"
                  value={newCategory.Kategorie}
                  onChange={e => setNewCategory({...newCategory, Kategorie: e.target.value})}
                />
              </div>
              <div className="flex items-center gap-2">
                <input 
                  type="checkbox" 
                  id="catActive"
                  checked={newCategory.IstAktiv}
                  onChange={e => setNewCategory({...newCategory, IstAktiv: e.target.checked})}
                />
                <label htmlFor="catActive" className="text-sm">Ist aktiv</label>
              </div>
              <button 
                type="submit"
                className="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 rounded-lg transition-colors"
              >
                Kategorie speichern
              </button>
            </form>
          </div>
        </div>
      )}

      {/* MATERIAL FORM MODAL */}
      {showMaterialForm && (
        <div className="fixed inset-0 bg-black/50 backdrop-blur-sm flex items-center justify-center p-4 z-50">
          <div className="bg-white dark:bg-zinc-900 rounded-2xl shadow-xl w-full max-w-sm overflow-hidden">
            <div className="p-6 border-b flex justify-between items-center">
              <h3 className="text-xl font-bold">Neues Material</h3>
              <button onClick={() => setShowMaterialForm(false)}><X size={24} /></button>
            </div>
            <form onSubmit={handleCreateMaterial} className="p-6 space-y-4">
              <div>
                <label className="block text-sm font-medium mb-1">Materialname</label>
                <input 
                  required
                  type="text" 
                  className="w-full bg-zinc-50 dark:bg-zinc-800 border rounded-lg px-3 py-2"
                  value={newMaterial.Material}
                  onChange={e => setNewMaterial({...newMaterial, Material: e.target.value})}
                />
              </div>
              <div className="flex items-center gap-2">
                <input 
                  type="checkbox" 
                  id="matActive"
                  checked={newMaterial.IstAktiv}
                  onChange={e => setNewMaterial({...newMaterial, IstAktiv: e.target.checked})}
                />
                <label htmlFor="matActive" className="text-sm">Verfügbar</label>
              </div>
              <button 
                type="submit"
                className="w-full bg-blue-600 hover:bg-blue-700 text-white font-bold py-3 rounded-lg transition-colors"
              >
                Material speichern
              </button>
            </form>
          </div>
        </div>
      )}
    </div>
  );
}
